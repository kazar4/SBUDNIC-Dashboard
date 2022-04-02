<script>
    import Button, { Label } from '@smui/button';

    import { getContext } from 'svelte';
	const { open } = getContext('simple-modal');

    import GalleryContent from './GalleryContent.svelte'
	const showSurprise = () => open(GalleryContent, {imageLinks: dataList});

    const changeImage = (change) => {

        let currIndex = 0
        for (let i in dataList) {
            let l = dataList[i]["link"]
            if (l === link) {
                currIndex = i
            }
        }

        let newIndex = parseInt(currIndex) + parseInt(change)
        //console.log(newIndex)
        if (newIndex < 0) {
            newIndex = dataList.length - 1
        } else if (newIndex > dataList.length - 1) {
            newIndex = 0
        }

        link = dataList[newIndex]["link"]

        //open(SingleImageGallery, {link: dataList[newIndex]["link"], fromGallery: true, dataList: dataList, date: date})
        };

    export let link = "";
    export let fromGallery = false;
    export let dataList = [];
    export let date = "";

    //console.log(link)

    let currRotation = 0

    function divHeight(currR) {
        if (currR % 180 === 0) {
            return "300px"
        } else {
            return "400px"
        }
    }

    //style={`transform: rotate(${currRotation}deg); height=${divHeight(currRotation)}`

    //width={divHeight(currRotation)}

    //<img src={link} alt={"Image From Satelite"}/>

    //ctx = document.getElementById("canvas").getContext("2d");
    //img = new Image();
    //img.src = link;
    //img.xpos = 0;
    //img.ypos = 0;

    import { Canvas, Layer, t } from "svelte-canvas";
import InnerGrid from '@smui/layout-grid/src/InnerGrid.svelte';

    $: render = ({ context, width, height }) => {
        var img = new Image();
        img.src = link;
        img.xpos = 0;
        img.ypos = 0;
        img.addEventListener('load', function() {
            //context.drawImage(img, img.xpos, img.ypos);

            context.clearRect(0,0,width,height);

            // save the unrotated context of the canvas so we can restore it later
            // the alternative is to untranslate & unrotate after drawing
            context.save();

            // move to the center of the canvas
            context.translate(width/2, height/2);

            // rotate the canvas to the specified degrees
            context.rotate(currRotation*Math.PI/180);

            // draw the image
            // since the context is rotated, the image will be rotated also
            /*
            let newScale = 1
            let newW = img.width * newScale
            let newH = img.height * newScale
            while (newW > width || newH > height || newW > height || newH > width) {
                newScale = newScale - 0.1
                newW = img.width * newScale
                newH = img.height * newScale
            } 
            */
            context.drawImage(img,-img.width/2,-img.height/2, img.width, img.height);

            // we’re done with the rotating so restore the unrotated context

            context.restore();
            //context.rotate(30 * Math.PI/180);
        }, false);
    };

    let w;
    let h;
    //<svelte:window bind:innerWidth={w} bind:innerHeight={h}/>
</script>

<div bind:clientWidth={w} bind:clientHeight={h}>
    <Button on:click={() => {currRotation = currRotation + 90}} color={"secondary"}>Flip Image</Button>
    {#if fromGallery}
        <Button on:click={() => showSurprise()} color={"secondary"}>Go Back to Gallery</Button>
        <Button on:click={() => changeImage(-1)} color={"secondary"}>Prev</Button>
        <Button on:click={() => changeImage(1)} color={"secondary"}>Next</Button>
    {/if}
    {#if fromGallery}
        <h3>{date}</h3>
    {:else}
        <h3>Image</h3>
    {/if}
    <div id={"canvas"}> 
        <Canvas width={w} height={h*0.7} on:click={() => {currRotation = currRotation + 90}}>
            <Layer {render}/>
        </Canvas>
    </div>
</div>
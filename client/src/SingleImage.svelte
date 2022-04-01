<script>
    import Button, { Label } from '@smui/button';

    export let link = "";
    console.log(link)

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
            context.drawImage(img,-img.width/2,-img.height/2, img.width * 1.3, img.height * 1.3);

            // we’re done with the rotating so restore the unrotated context
            context.restore();

            //context.rotate(30 * Math.PI/180);
        }, false);
    };

</script>
  
<div>
    <Button on:click={() => {currRotation = currRotation + 90}}>Flip Image</Button>
    <div id={"canvas"}> 
        <Canvas width={400} height={400}>
            <Layer {render}/>
        </Canvas>
    </div>
</div>
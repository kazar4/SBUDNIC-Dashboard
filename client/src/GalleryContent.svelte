<script>
	import Carousel from "./Carousel.svelte";
	import { onMount } from 'svelte';

	export let imageLinks = [];

	function reverse(s){
    	return s.split("").reverse().join("");
	}

	let newLinks = []
	let date = ""
	for (let i in imageLinks) {
		let fileName = imageLinks[i]["fileName"]
		let dateStr = fileName.slice(0, fileName.length - 5)
		
		let dateStrAsListReverse = dateStr.split("").reverse()
		dateStrAsListReverse[reverse(dateStr).indexOf("-")] = ":"
		dateStrAsListReverse[dateStrAsListReverse.indexOf("-")] = ":"

		dateStr = dateStrAsListReverse.reverse().join("");
		//console.log(dateStr)

		date = new Date(dateStr)
		//console.log(date.toString())

		newLinks.push({"path":imageLinks[i]["link"], "name": date.toString().slice(0, date.toString().indexOf("GMT"))})
	}

	let w;
	let h;
	let ImageSpread = []

	onMount(() => {
		console.log(w)
		const chunkSize = parseInt(w/250);
		for (let i = 0; i < newLinks.length; i += chunkSize) {
			ImageSpread.push(newLinks.slice(i, i + chunkSize));
		}
		ImageSpread = ImageSpread //updates state as push does not
	})

	//console.log(ImageSpread)
	//<svelte:window bind:innerWidth={w} bind:innerHeight={h}/>
</script>



<div id="imageGallery" bind:clientWidth={w} bind:clientHeight={h}>
	{#each ImageSpread as images, i}
		<div>
			<Carousel {images} {imageLinks} {date} imageHeight={140} imageSpacing={15}/>
		</div>
	{/each}
</div>

<style>

	div {
		padding-bottom: 10px;
	}

	div:last-child {
		padding-bottom: 0px;
	}

</style>
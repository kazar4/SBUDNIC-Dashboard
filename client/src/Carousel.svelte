<script>
	export let images;
	export let imageHeight = 150;
	export let imageSpacing = 0;

	import { getContext } from 'svelte';
	import SingleImage from './SingleImage.svelte';
	const { open } = getContext('simple-modal');
	const showImage = (link) => open(SingleImage, { link: link, fromGallery: true, dataList: imageLinks, date: date});

	export let imageLinks = []
	export let date = ""
</script>

<div class="carousel">
	<div class="carousel__container">
		{#each images as image, i}
			<div class="imageContainer">
				<img
					src={image.path}
					alt={image.alt}
					id={image.id}
					style={`height: ${imageHeight}px; margin-right: ${imageSpacing}px`}
					on:click={() => showImage(image.path)}
				/>
				<div class="imageName" style={`margin-right: ${imageSpacing}px`}>{image.name}</div>
			</div>
		{/each}
	</div>
</div>

<style>
	.carousel {
		display: flex;
		overflow-x: auto;
		position: relative;
		width: 100%;
	}
	.carousel__container {
		display: flex;
	}

	.imageContainer {
		display: flex;
		flex-direction: column;
		text-align: center;
	}

	img {
		transition: transform 250ms ease;
		transform: scale(100%)
	}

	img:hover {
		transform: scale(104%);
		cursor: pointer;
	}

	.imageName {
		
	}
</style>
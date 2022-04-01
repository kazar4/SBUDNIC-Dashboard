<script>
	import Card, {
    Content,
    PrimaryAction,
    Actions,
    ActionButtons,
    ActionIcons,
  	} from '@smui/card';
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import { getContext } from 'svelte';
	import GalleryContent from './GalleryContent.svelte';

	import Popup from './Popup.svelte';
	const { open } = getContext('simple-modal');
	const showSurprise = () => open(GalleryContent, { imageLinks: dataList });
	/*
	let address = "http://localhost:1220/getGalleryLinkList"
	let dataList = []
	function fetchJsonRepeat(address, delayM) {
			fetch(address).then((res) => res.json()).then((json) => {
			dataList = json["data"]
			// console.log(dataList)
			// console.log(json)
			// setTimeout(() => fetchJsonRepeat(address), delayM);
			// have json variable be a reactive state
			// rerender each array in html given that json array
		});
	}
	fetchJsonRepeat(address, 5000)
	*/
</script>


<div>
	<Card padded>
		<PrimaryAction on:click={showSurprise} padded>
				Open Telemetry (TODO)
		  </PrimaryAction>
	</Card>
</div>

<style>
</style>
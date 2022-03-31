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
	import Popup from './Popup.svelte';
	const { open } = getContext('simple-modal');
	const showSurprise = () => open(Popup, { message: "It's a modal!" });

	/*
	let address = ""
	let json = {}
	function fetchJsonRepeat(address, delayM) {
			fetch(address).then((res) => res.json()).then((json) => {
			console.log(json)
			setTimeout(() => fetchJsonRepeat(address), delayM);
			// have json variable be a reactive state
			// rerender each array in html given that json array
		});
	}
	fetchJsonRepeat(address, 10000)
	*/
</script>


<div>
	<Card padded>
		<PrimaryAction on:click={showSurprise} padded>
				Open Gallery
		  </PrimaryAction>
	</Card>
</div>

<style>

</style>
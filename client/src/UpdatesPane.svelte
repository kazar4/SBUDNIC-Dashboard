<script>
	import Card, {
    Content,
    PrimaryAction,
    Actions,
    ActionButtons,
    ActionIcons,
  	} from '@smui/card';
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import Button, { Label } from '@smui/button';
  	import IconButton, { Icon } from '@smui/icon-button';

	import { getContext } from 'svelte';
	import SingleImage from './SingleImage.svelte';
	const { open } = getContext('simple-modal');
	const showImage = (link) => open(SingleImage, { link: link });
	
	let address = "http://localhost:1220/getCommandData"
	let dataList = []
	function fetchJsonRepeat(address, delayM) {
			fetch(address).then((res) => res.json()).then((json) => {
			dataList = json["data"]
			// console.log(json)
			// setTimeout(() => fetchJsonRepeat(address), delayM);
			// have json variable be a reactive state
			// rerender each array in html given that json array
		});
	}
	fetchJsonRepeat(address, 5000)
	
</script>


<div class={"updates"}>
	{#each dataList as row, i}
		<div class={"update"}>
			<Cell span={12}>
				{#if row["imageLink"] !== ""}
					<Card padded> 
						<div>{row["command"].trim()}</div>
						<div>{row["extraMessage"].trim()}</div>
						<Actions fullBleed>
							<Button on:click={() => {
								console.log(row["imageLink"]);
								showImage(row["imageLink"])
							}} color="secondary">
							  <Label>Show Image</Label>
							  <i class="material-icons" aria-hidden="true">arrow_forward</i>
							</Button>
						</Actions>
					</Card>
				{:else if true}
					<Card padded> 
						<div>{row["command"].trim()}</div>
						<div>{row["extraMessage"].trim()}</div>
					</Card>
				{:else}
					<Card padded> 
						<div>{row["command"].trim()}</div>
						<div>{row["extraMessage"].trim()}</div>
					</Card>
				{/if}
			</Cell>
		</div>
	{/each}
</div>

<style>

	.updates {
		padding: 20px;
		height: 400px;
		overflow-y:auto
	}

	.updates > .update {
		margin-top: 20px;
	}

	.updates > .update:first-child {
		margin: 0;
	}
</style>
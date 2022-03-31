<script>
	import Card, { Content } from "@smui/card";
	import LayoutGrid, { Cell } from '@smui/layout-grid';

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
	fetchJsonRepeat(address, 5000)
	*/
</script>


<div class={"updates"}>
	{#each Array(8) as _unused, _i}
		<div class={"update"}>
			<Cell span={12}>
					<Card padded> Updates </Card>
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
<script>
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import MediaQuery from "./MediaQuery.svelte";
</script>

<LayoutGrid>
	<Cell spanDevices={{desktop:6, tablet: 12, phone: 12}}>
		<h1>SBUDNIC Dashboard</h1>
	</Cell>
	<MediaQuery query="(min-width: 850px)" let:matches>
		{#if matches}
		<Cell spanDevices={{desktop:6, tablet: 0, phone: 0}}>
			<img src="https://sbudnic.space/static/media/sbudnicN.aeb9041e.png" alt="SBUDNIC logo" height="200px">
		</Cell>
		{/if}
	</MediaQuery>
</LayoutGrid>

<style>
	h1 {
			font-family: 'Nunito', sans-serif;
			color: #2b2a2e;
			font-size: 3.5em;
			text-align: center;
		}
</style>
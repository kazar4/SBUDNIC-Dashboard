<script>
	import Card, { Content } from "@smui/card";
	import LayoutGrid, { Cell } from '@smui/layout-grid';
	import SBanner from "./SBanner.svelte";
	import LogoDetails from "./LogoDetails.svelte";
	import UpdatesPane from "./UpdatesPane.svelte";
	import GalleryPane from "./GalleryPane.svelte";
	import TelemetryPane from "./TelemetryPane.svelte"
</script>
	

<div>
    <SBanner></SBanner>
    <main>
        <LogoDetails/>

        <LayoutGrid>
            <Cell span={6}>
                <UpdatesPane/>
            </Cell>
            <Cell span={6}>
				<div class={"dataPanes"}>
					<div class={"dataCard"}>
						<GalleryPane/>
					</div>
					<div class={"dataCard"}>
						<TelemetryPane/>
					</div>
				</div>
            </Cell>
        </LayoutGrid>
    </main>
</div>

<style>
	main {
		text-align: center;
		padding: 1em;
		margin: 0 auto;
	}

	.dataPanes > .dataCard {
		margin-bottom: 20px;
	}

	.dataPanes > .dataCard:last-child {
		margin-bottom: 0px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<svelte:head>

	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Nunito&display=swap" rel="stylesheet">

	<!-- Fonts -->
	<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,600,700">
		
	<!-- Material Typography -->
		<link rel="stylesheet" href="https://unpkg.com/@material/typography@13.0.0/dist/mdc.typography.css" />
		
	<!-- SMUI -->
	<link rel="stylesheet" href="https://unpkg.com/svelte-material-ui/bare.css" />

	<!-- Material Icons -->
	<link
	rel="stylesheet"
	href="https://fonts.googleapis.com/icon?family=Material+Icons"
	/>
	<!-- Roboto -->
	<link
	rel="stylesheet"
	href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,600,700"
	/>
	<!-- Roboto Mono -->
	<link
	rel="stylesheet"
	href="https://fonts.googleapis.com/css?family=Roboto+Mono"
	/>
</svelte:head>
<template>
	<div class="grid-box">
		<div class="header">
			<Header />
		</div>

		<div class="info">
			<Info />
		</div>

		<div class="video">
			<VideoStream />
		</div>

		<div class="data">
			<div class="center">
				<h2>Sensoren</h2>
				<DataElement title="Temperatur" mapKey="temperature" />
				<br />
				<DataElement title="Luftfeuchtigkeit" mapKey="humidity" />
				<br />
				<DataElement title="Sensor 3" mapKey="sensor3" />
			</div>
		</div>
	</div>
</template>

<script>
import VideoStream from "@/components/VideoStream.vue"
import Header from "@/components/Header.vue"
import DataElement from "@/components/DataElement.vue"
import Info from "@/components/Info.vue"

export default {
	name: "App",
	components: {
		VideoStream,
		Header,
		DataElement,
		Info,
	},
}
</script>

<style>
:root {
	--fg-color: #2b3d55;
	--bg-color: white;
	--bar-bg-color: #2b3d55;
	--bar-fg-color: white;
	--container-bg-color: #eaeaea;
	--red: #d61e27;
	color-scheme: light, dark;
}

* {
	margin: 0;
	padding: 0;
}

html,
body {
	width: 100%;
	height: 100%;
	color: var(--fg-color);
	background: var(--bg-color);
}

#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}
</style>

<style scoped>
.grid-box {
	display: grid;
	width: 100%;
	height: 100vh;
	grid-template-columns: 50% 50%;
	grid-template-rows: 7% 35% 55%;
	grid-template-areas:
		"header header"
		"info info"
		"video data";
}

.header {
	grid-area: header;
	background: var(--bar-bg-color);
}

.info {
	grid-area: info;
}

.video {
	grid-area: video;
}

.data {
	padding: 5%;
	grid-area: data;
}

.center h2 {
	font-size: 20pt;
	text-align: center;
	margin-bottom: 4%;
}

.center {
	position: relative;
	top: 50%;
	transform: translateY(-50%);
}

.footer {
	grid-area: footer;
}

@media screen and (max-width: 950px) {
	/* responsive layout */
	.grid-box {
		height: 100%;
		grid-template-columns: 100%;
		grid-template-rows: 6% 36% 29% 29%;
		grid-template-areas:
			"header"
			"info"
			"video"
			"data";
	}

	.center h2 {
		font-size: 18pt;
	}
}

@media screen and (max-width: 365px) {
	.grid-box {
		grid-template-rows: 5% 45% 25% 25%;
	}
}
</style>

<template>
	<div class="container">
		<p>{{ title }}:</p>
		<p>{{ value }}</p>
	</div>
</template>

<script>
export default {
	name: "DataElement",
	props: {
		title: {
			type: String,
			required: true,
		},
		mapKey: {
			type: String,
			required: true,
		},
	},
	data() {
		return {
			value: String,
		}
	},
	mounted() {
		fetch("http://127.0.0.1:8080/sensor_data_api")
			.then((resp) => resp.json())
			.then((data) => (this.value = data[this.mapKey]))
			.catch((err) => console.log(err.message))
	},
}
</script>

<style scoped>
.container {
	background: var(--container-bg-color);
	border-radius: 10px;
	width: 40%;
	padding: 3% 4%;
	margin: auto;
	display: flex;
	justify-content: space-between;
	align-content: center;
}

.container p {
	font-size: 14pt;
	display: inline-block;
}

@media screen and (max-width: 950px) {
	.container {
		width: 50%;
	}

	.container p {
		font-size: 12pt;
	}
}
</style>

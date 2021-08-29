<template>
	<div class="container">
		<p>
			Orci pellentesque blandit bibendum felis sollicitudin mollis facilisi netus torquent.
			Malesuada ridiculus auctor condimentum fermentum lacinia est mi tortor metus. Facilisi
			egestas vivamus facilisis justo tincidunt amet ipsum semper nunc! Eget risus velit
			suscipit etiam id suspendisse phasellus proin magnis. At nec fames in vulputate
			vestibulum dis sapien tortor platea. Cras suspendisse, eget volutpat in mattis aliquet
			suscipit faucibus fringilla. Nulla nostra et erat laoreet parturient semper posuere
			sociis sociosqu.
		</p>
	</div>
</template>

<script>
export default {
	name: "Info",
}
</script>

<style scoped>
.container {
	padding: 5% 20%;
	max-height: 100%;
}

p {
	text-align: justify;
	line-height: 1.4;
	font-size: 14pt;
}

@media screen and (max-width: 580px) {
	p {
		font-size: 12pt;
	}

	.container {
		padding: 5% 10%;
	}
}
</style>

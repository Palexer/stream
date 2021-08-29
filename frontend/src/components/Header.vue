<template>
	<link
		rel="stylesheet"
		href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
	/>
	<div class="bar">
		<p>Bienen Beobachtung</p>
		<div class="icons">
			<label class="toggle" @click="toggleTheme()">
				<i class="fa fa-adjust"></i>
			</label>
			<a href="https://github.com/Palexer/" target="_blank"><i class="fa fa-github"></i></a>
		</div>
	</div>
</template>

<script>
export default {
	name: "Header",
	data() {
		return {
			theme: "",
		}
	},
	mounted() {
		this.theme = localStorage.theme
		if (this.theme == null) {
			this.theme = "light"
		}
		if (this.theme == "dark") {
			this.setDarkTheme()
		}
	},
	watch: {
		theme(newValue) {
			localStorage.theme = newValue
		},
	},
	methods: {
		setDarkTheme() {
			let root = document.documentElement
			root.style.setProperty("--fg-color", "white")
			root.style.setProperty("--bg-color", "#283038")
			root.style.setProperty("--container-bg-color", "#1a1f24")
			this.theme = "dark"
		},
		setLightTheme() {
			let root = document.documentElement
			root.style.setProperty("--fg-color", "#2b3d55")
			root.style.setProperty("--bg-color", "white")
			root.style.setProperty("--container-bg-color", "#eaeaea")
			this.theme = "light"
		},
		toggleTheme() {
			if (this.theme == "light") {
				this.setDarkTheme()
			} else {
				this.setLightTheme()
			}
		},
	},
}
</script>

<style scoped>
.bar {
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center; /* align vertical */
	justify-content: space-between;
}

.bar p {
	color: var(--bar-fg-color);
	font-size: 18pt;
	margin: 2%;
}

.icons {
	display: flex;
	justify-content: center;
	align-content: center;
	margin: 2%;
}

.icons a {
	font-size: 20pt;
	color: var(--bar-fg-color);
	text-decoration: none;
	margin-left: 30%;
}

.icons a:hover {
	transition: 0.2s;
	color: #d2d2d2;
}

.toggle {
	color: var(--bar-fg-color);
	font-size: 20pt;
}

.toggle:hover {
	transition: 0.2s;
	color: #d2d2d2;
	cursor: pointer;
}

@media screen and (max-width: 950px) {
	.bar p {
		font-size: 16pt;
	}
}
</style>

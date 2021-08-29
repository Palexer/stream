<template>
	<div class="container">
		<img src="http://127.0.0.1:8080/video_stream" @click="showModal()" ref="normalImg" />
	</div>

	<!-- The Modal -->
	<div id="myModal" class="modal" ref="modal">
		<span class="close" @click="closeModal()">&times;</span>
		<img class="modal-content" id="imgContent" ref="largeImage" />
	</div>
</template>

<script>
export default {
	name: "VideoStream",
	methods: {
		showModal() {
			this.$refs.modal.style.display = "block"
			this.$refs.largeImage.src = this.$refs.normalImg.src
		},

		closeModal() {
			this.$refs.modal.style.display = "none"
		},
	},
	created() {
		document.addEventListener("keydown", (event) => {
			if (event.key == "Escape") {
				this.closeModal()
			}
		})
	},
}
</script>

<style scoped>
.container {
	width: 100%;
	height: 100%;
}

img {
	width: 100%;
	height: 100%;
	display: flex;
	object-fit: contain;
}

img:hover {
	cursor: pointer;
}

/* The Modal (background) */
.modal {
	display: none; /* Hidden by default */
	position: fixed; /* Stay in place */
	z-index: 1; /* Sit on top */
	left: 0;
	top: 0;
	width: 100%; /* Full width */
	height: 100%; /* Full height */
	overflow: auto; /* Enable scroll if needed */
	background-color: rgb(0, 0, 0); /* Fallback color */
}

/* Modal Content (image) */
.modal-content {
	margin: auto;
	display: inline-block;
	vertical-align: middle;
	height: 100%;
	max-width: 100%;
	max-height: 100%;
	object-fit: contain;
}

/* Add Animation */
.modal-content {
	-webkit-animation-name: zoom;
	-webkit-animation-duration: 0.6s;
	animation-name: zoom;
	animation-duration: 0.6s;
}

@-webkit-keyframes zoom {
	from {
		-webkit-transform: scale(0);
	}
	to {
		-webkit-transform: scale(1);
	}
}

@keyframes zoom {
	from {
		transform: scale(0);
	}
	to {
		transform: scale(1);
	}
}

/* The Close Button */
.close {
	position: absolute;
	top: 15px;
	right: 35px;
	color: #f1f1f1;
	font-size: 40px;
	font-weight: bold;
	transition: 0.3s;
}

.close:hover,
.close:focus {
	color: var(--red);
	text-decoration: none;
	cursor: pointer;
}
</style>

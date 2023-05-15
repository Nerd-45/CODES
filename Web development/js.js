// document.querySelector(".container").addEventListener("click",()=>{
// document.querySelector(".sun-logo").classList.toggle("animate-sun");
// document.querySelector(".moon-logo").classList.toggle("animate-moon");
// document.querySelector("body").classList.toggle("dark");
// })
<script>
// Get the video
var video = document.getElementById("myVideo");

// Get the button
var btn = document.getElementById("myBtn");

// Pause and play the video, and change the button text
function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}
</script>
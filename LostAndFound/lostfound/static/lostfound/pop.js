let a1 = document.getElementById("btn");

a1.addEventListener("click", (e) => {
  createpop("new-lost-item", 830, 700);
});

function createpop(url, height, width) {
  let top = (screen.height - height) / 4;
  let left = (screen.width - width) / 2;
  let extra = `height=${height}px,width=${width}px,popup,top=${top},left=${left}`;
  window.alert("Please enter the details carefully");
  window.open(url, "_blank", extra);
}

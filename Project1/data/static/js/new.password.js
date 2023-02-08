function checkPassword(){
  let id_new_password1 = document.getElementById
  ("id_new_password1").value;
  let id_new_password2 = document.getElementById
  ("id_new_password2").value;
  console.log(id_new_password1,id_new_password2);
}
  if(id_new_password1.length != 8){
    if( id_new_password1 == id_new_password2){
      message.textContent = "Şifrəniz yenilənir...";
      message.style.backgroundColor = "#279d0d";
      message.style.borderRadius = "9px";
    }
  }
<template>
    <nav class="navbar navbar-light bg-light navbar-expand-lg custom-nav" id="navbar">
        <a class="navbar-brand" id="nbrand" href="#">Aluma<b>Meet</b></a>
            <div class="navbar-collapse">
            <ul class="navbar-nav flex-row ml-auto justify-content-between" id="list">
                <li class="nav-item">
                    <a class="nav-link" href="/feed"><button class="navbutton active"><i class="fa fa-home"></i></button></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link"><button class="navbutton"><i class="fa fa-search"></i></button></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/profile"><button class="navbutton"><i class="fa fa-user-circle-o"></i></button></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/messages"><button class="navbutton"><i class="fa fa-envelope"></i></button></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link"><button class="navbutton" @click="logout"><i class="fa fa-power-off"></i></button></a>
                </li>            
            </ul>
            </div>
    </nav>
</template>
<script>
// eslint-disable-next-line no-unused-vars
import $ from 'jquery'
export default {
  name: 'Navbar',
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({ name: 'Home' });
    },
  },
  mounted() {
      $(window).resize(function () {
          if($(window).width()<992){
              $("#navbar").addClass('fixed-bottom');
              $("#list").removeClass('ml-auto');
              $("#list").addClass('mx-auto');
              $("#nbrand").hide();
          }
          else{
              $("#navbar").removeClass('fixed-bottom');
              $("#list").removeClass('mx-auto');
              $("#list").addClass('ml-auto');
              $("#nbrand").show();
          }
      });
      $(document).ready(function () {
          if($(window).width()<992){
              $("#navbar").addClass('fixed-bottom');
              $("#list").removeClass('ml-auto');
              $("#list").addClass('mx-auto');
              $("#nbrand").hide();
          }
          else{
              $("#navbar").removeClass('fixed-bottom');
              $("#list").removeClass('mx-auto');
              $("#list").addClass('ml-auto');              
              $("#nbrand").show();
          }
      })
  }
};
</script>

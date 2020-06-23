<template>
    <nav class="navbar navbar-light bg-light navbar-expand-lg" style="background-color:transparent !important; border-bottom: 1px solid #d5d5d5">
        <a class="navbar-brand" href="#">Aluma<b>Meet</b></a>
        <button class="navbar-toggler btn btn-outline-dark" type="button" data-trigger="#main_nav">
           <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
         </button>
        <div class="navbar-collapse" id="main_nav" align="center">
            <ul class="navbar-nav ml-auto">
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
            <div class="offcanvas-header mt-3">
                    <button class="close-btn"><i class="fa fa-times-circle-o"></i></button><br>
                </div>
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
      $(function () {
    'use strict'
	$("[data-trigger]").on("click", function(){
        var trigger_id =  $(this).attr('data-trigger');
        $(trigger_id).toggleClass("show");
        $('body').toggleClass("offcanvas-active");
        $('#content').hide();
    });

    // close if press ESC button 
    $(document).on('keydown', function(event) {
        if(event.keyCode === 27) {
           $(".navbar-collapse").removeClass("show");
           $("body").removeClass("overlay-active");
           $('#content').show();
        }
    });

    // close button 
    $(".close-btn").click(function(){
        $(".navbar-collapse").removeClass("show");
        $("body").removeClass("offcanvas-active");
        $('#content').show();
    }); 
})
  }
};
</script>

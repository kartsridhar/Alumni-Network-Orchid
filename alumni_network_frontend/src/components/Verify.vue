<template>
    <div>
        <nav class="navbar navbar-light bg-light navbar-expand-lg custom-nav" id="navbar">
        <a class="navbar-brand" id="nbrand" href="#">Aluma<b>Meet</b></a>
            <div class="navbar-collapse">
            <ul class="navbar-nav ml-auto" id="list">
                <li class="nav-item">
                    <a class="nav-link"><button class="navbutton" @click="logout"><i class="fa fa-power-off"></i></button></a>
                </li>            
            </ul>
            </div>
    </nav>
       <mbnav/>
 
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="aluma-card" style="margin-top:20px;" align="center">
                      <h1>Verify Your Email</h1>
                        <form class="p-2" @submit.prevent="verify">
                            <div class="alert alert-info">We have sent a verification mail to your registered email-id please verify to continue.</div>
                            <input id="otp" class="form-control mb-3" type="text" placeholder="OTP" required v-model="code">
                            <div id="errmsg" class="alert alert-danger" style="display:none;"></div>
                            <div id="errmsg1" class="alert alert-danger" style="display:none;"></div>
                            <button class="btn btn-dark btn-block my-4 float-center" type="submit">Verify</button>
                        </form>
              
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import $ from 'jquery';
import jwtDecode from 'jwt-decode';
import axios from 'axios';
import MobileNavbar from './MobileNavbar.vue'
export default {
    name: 'Verify',
    data(){
        return {
            code: '',
        }
    },
    components: {
        'mbnav': MobileNavbar,
    },
    methods: {
        logout() {
            localStorage.clear();
            this.$router.push({ name: 'Home' });
        },
        verify() {
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                email:user_decode.identity.email,
                confirmation_code:this.code,
            };
            const path= 'http://localhost:5000/verify';
            axios.post(path,payload).then((res) => {
                if(res.data!="1"){
                    this.$router.push({ name: 'Feed' });
                    }
                else{
                    $("#errmsg").html("Please Check the code and try again!!").fadeIn("slow").delay(3000).fadeOut("slow");
                }
                })
            .catch((err) => {
                alert(err);
            });
        },
     },
    mounted() {
        $("#otp").keypress(function (e) {
            if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                $("#errmsg").html("Numeric Values only Allowed").fadeIn("slow").delay(3000).fadeOut("slow");
                return false;
            }
            var len=$(this).val().length;
            if(len>3){
                $("#errmsg1").html("Please Enter a 4 digit number").fadeIn("slow").delay(3000).fadeOut("slow");
                return false;
            }
        });

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
}
</script>
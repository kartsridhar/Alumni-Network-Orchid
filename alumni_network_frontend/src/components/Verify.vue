<template>
    <div>
        <nav class="navbar navbar-light bg-light navbar-expand-lg" style="background-color:transparent !important; border-bottom: 1px solid #d5d5d5">
            <a class="navbar-brand" href="#">Aluma<b>Meet</b></a>
            <button class="navbar-toggler btn btn-outline-dark" type="button" data-trigger="#main_nav">
                <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
            </button>
            <div class="navbar-collapse" id="main_nav" align="center">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link"><button class="navbutton" @click="logout"><i class="fa fa-power-off"></i></button></a>
                    </li>            
                </ul>
                <div class="offcanvas-header mt-3">
                    <button class="close-btn"><i class="fa fa-times-circle-o"></i></button><br>
                </div>
             </div>
        </nav>
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

export default {
    name: 'Verify',
    data(){
        return {
            code: '',
        }
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
                alert(res);
                this.$router.push({ name: 'Feed' });
                })
            .catch((err) => {
                alert(err);
            });
        },
     },
    mounted() {
        $("#otp").keypress(function (e) {
            if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                $("#errmsg").html("Numeric Values only Allowed").fadeIn("slow").fadeOut("slow");
                return false;
            }
        });
        $("#otp").keypress(function () {
            var len=$(this).val().length;
            if(len>3){
                $("#errmsg1").html("Please Enter a 4 digit number").fadeIn("slow").fadeOut("slow");
                return false;
            }
        });
    },
}
</script>
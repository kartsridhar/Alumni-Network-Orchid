<template>
<div>
    <nav class="navbar navbar-light bg-light" style="background-color:transparent !important;">
  <a class="navbar-brand" href="#">
    <img src="../assets/logo.png" width="70" height="70" alt="">
    Aluma<b>Meet</b>
  </a>
</nav>
    <div class="container-fluid">
        <div class="row" style="padding-top:30px;">
            <div class="col-lg-6 offset-lg-3 sm-auto md-auto">
                <div class="card border-dark text-center">
                    <div class="card-header bg-transparent">
                        <div class="nav nav-tabs nav-justified card-header-tabs">
                            <span class="nav-item nav-link active" id="nav-signup-tab" data-toggle="tab" href="#nav-signup" role="tab" aria-controls="nav-signup" aria-selected="false">Signup</span>
                            <span class="nav-item nav-link" id="nav-login-tab" data-toggle="tab" href="#nav-login" role="tab" aria-controls="nav-login" aria-selected="true">Login</span>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="tab-content" id="nav-tabContent">
                            <div class="tab-pane fade" id="nav-login" role="tabpanel" aria-labelledby="nav-login-tab">
                                <div class="row">
                                    <div class="col-lg-6  sm-auto md-auto">
                                    <div class="contaainer-fluid"><img src="../assets/login.jpg" class="img-fluid rounded"></div>
                                    </div>
                                    <div class="col-lg-6 sm-auto md-auto">
                                        <form class="p-3" style="margin-top:40px" v-on:submit.prevent="signIn">
                                            <input type="email" id="defaultLoginFormEmail" class="form-control mb-4" placeholder="E-mail">
                                            <input type="password" id="defaultLoginFormPassword" class="form-control mb-4" placeholder="Password">
                                            <button class="btn btn-dark btn-block my-4" type="Login">Sign in</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade show active" id="nav-signup" role="tabpanel" aria-labelledby="nav-signup-tab">
                                    <div class="row">
                                        <div class="col-lg-6  sm-auto md-auto">
                                            <div class="contaainer-fluid"><img src="../assets/signup.png" class="img-fluid rounded"></div>
                                        </div>
                                        <div class="col-lg-6 sm-auto md-auto">
                                            <form class="p-2" v-on:submit.prevent="signUp">
                                                <input class="form-control mb-5" v-model="signUpName" id="name" type="text" placeholder="Name" required>
                                                <input class="form-control mb-5" v-model="signUpUsername" id="username" type="text" placeholder="Username" required>
                                                <input type="email" v-model="signUpEmail" id="defaultSignupFormEmail" class="form-control mb-5" placeholder="E-mail" required>
                                                <input type="password" v-model="signUpPass" id="defaultSignupFormPassword" class="form-control mb-5" placeholder="Password" required>
                                                <button class="btn btn-dark btn-block my-4" type="submit">SIGN UP</button>
                                            </form>
                                        </div>
                                    </div>    
                                </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>
<script>
const axios = require('axios')

export default {
    name : 'Home',
    data () {
        return {
            // SIGN UP FORM MODELS
            signUpName: '',
            signUpUsername: '',
            signUpEmail: '',
            signUpPass: '',
        }
    },
    methods: {
        signUp () {
            axios.post('http://localhost:5000/signup',
                { email : this.signUpEmail,
            full_name : this.signUpName, 
            user_name : this.signUpUsername, 
            password : this.signUpPass, 
            }).then(res => {
                // Clearing the fields
                this.signUpName = ''
                this.signUpUsername = ''
                this.signUpEmail = ''
                this.signUpPass = ''
                console.log(res)
            })
            .catch(err => {
                console.log(err)
            })
        },
    }
}
</script>
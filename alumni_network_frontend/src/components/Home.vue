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
                            <span class="nav-item nav-link active" id="nav-signup-tab" data-toggle="tab" href="#nav-signup" role="tab" aria-controls="nav-signup" aria-selected="false" style="cursor: pointer;"><strong>Sign Up</strong></span>
                            <span class="nav-item nav-link" id="nav-login-tab" data-toggle="tab" href="#nav-login" role="tab" aria-controls="nav-login" aria-selected="true" style="cursor: pointer;"><strong>Login</strong></span>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="tab-content" id="nav-tabContent">
                            <div class="tab-pane fade" id="nav-login" role="tabpanel" aria-labelledby="nav-login-tab">
                                <div class="row">
                                    <div class="col-lg-6  sm-auto md-auto">
                                    <div class="container-fluid"><img src="../assets/login.jpg" class="img-fluid rounded"></div>
                                    </div>
                                    <div class="col-lg-6 sm-auto md-auto">
                                        <form class="p-3" style="margin-top:40px" @submit.prevent="login">
                                            <input type="email"  class="form-control mb-4" placeholder="E-mail" v-model="lEmail" required>
                                            <input type="password" class="form-control mb-4" placeholder="Password" v-model="lPass" required>
                                            <button class="btn btn-dark btn-block my-4" type="submit">Login</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade show active" id="nav-signup" role="tabpanel" aria-labelledby="nav-signup-tab">
                                    <div class="row">
                                        <div class="col-lg-6  sm-auto md-auto">
                                            <div class="container-fluid"><img src="../assets/signup.png" class="img-fluid rounded"></div>
                                        </div>
                                        <div class="col-lg-6 sm-auto md-auto">
                                            <form class="p-2" @submit.prevent="signup">
                                                <input class="form-control mb-5" type="text" placeholder="Name" v-model="sName" required>
                                                <input class="form-control mb-5" id="username" type="text" placeholder="Username" v-model="sUsername" required>
                                                <input type="email" id="defaultSignupFormEmail" class="form-control mb-5" placeholder="E-mail" v-model="sEmail" required>
                                                <input type="password" id="defaultSignupFormPassword" class="form-control mb-5" placeholder="Password" v-model="sPass" required>
                                                <button class="btn btn-dark btn-block my-4" type="submit">Sign Up</button>
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
import axios from 'axios';
import EventBus from './EventBus.vue';
import jwtDecode from 'jwt-decode';

export default {
    name : 'Home',
    data() {
        return {
            sName: '',
            sUsername: '',
            sEmail: '',
            sPass: '',
            lEmail: '',
            lPass: '',
        }
    },
    methods: {
        signup() {
            const payload = {
                email: this.sEmail,
                password: this.sPass,
                full_name: this.sName,
                user_name: this.sUsername,
            };
            console.log(payload)
            const path = 'http://localhost:5000/signup';
            axios.post(path, payload).then((res) => {
                localStorage.setItem('usertoken', res.data);
                this.$router.push({ name: 'Verify' });
            })
            .catch((err) => {
                alert(err);
            })
            this.emitMethod();
        },
        emitMethod() {
            EventBus.$emit('logged-in', 'loggedin');
        },
        login() {
            const payload = {
                email: this.lEmail,
                password: this.lPass,
            };
            console.log(payload)
            const path = 'http://localhost:5000/login';
            axios.post(path, payload).then((res) => {
                localStorage.setItem('usertoken', res.data);
                const cstat=jwtDecode(res.data).identity.confirmation_status;
                if(cstat===1){
                    this.$router.push({ name: 'Feed' });
                }
                else{
                    this.$router.push({ name: 'Verify' });
                }
            })
            .catch((err) => {
                alert(err);
            })
            this.emitMethod();
        },
    }
}
</script>
<template>
<div>
    <nav class="navbar navbar-light bg-light" style="background-color:white !important; border-bottom:1px solid #d5d5d5;">
  <a class="navbar-brand" href="#">
    Aluma<b>Meet</b>
  </a>
</nav>
    <div class="container-fluid">
        <div class="row" style="padding-top:30px;">
            <div class="col-lg-4 offset-lg-4 sm-auto md-auto">
                <div class="card border-grey">
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
                                    <div class="col-lg-12 sm-auto md-auto">
                                        <form class="p-3" @submit.prevent="login">
                                            <label>Email</label>
                                            <input type="email"  class="form-control mb-4"  v-model="lEmail" required>
                                            <label>Password</label>
                                            <input type="password" class="form-control mb-4"  v-model="lPass" required>
                                            <button class="btn btn-dark float-right" type="submit">Login</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade show active" id="nav-signup" role="tabpanel" aria-labelledby="nav-signup-tab">
                                    <div class="row">
                                        <div class="col-lg-12 sm-auto md-auto">
                                            <form class="p-2" @submit.prevent="signup">
                                                <label>Name</label>
                                                <input class="form-control mb-4" type="text"  v-model="sName" required>
                                                <label>Username</label>
                                                <input class="form-control mb-4" id="username" type="text"  v-model="sUsername" required>
                                                <label>Email</label>
                                                <input type="email" id="defaultSignupFormEmail" class="form-control mb-4"  v-model="sEmail" required>
                                                <label>Password</label>
                                                <input type="password" id="defaultSignupFormPassword" class="form-control mb-4"  v-model="sPass" required>
                                                <button class="btn btn-dark float-right" type="submit">Sign Up</button>
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
            const path = 'https://localhost:5000/signup';
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
            const path = 'https://localhost:5000/login';
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
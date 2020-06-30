<template>
    <div>
        <navbar/>
        <mbnav/>
            <div class="container-fluid">
                <div class="row" id="content">
                    <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                        <div class="aluma-card" style="margin-top:20px;" align="center">
                            <div class="aluma-card-img">
                                <img src="../assets/profile.png" class="img-fluid rounded-circle bordered" height="150" width="150"><br><br>
                            </div>
                            <div class="aluma-card-profile" align="left" style="margin-top:10px">
                                <span class="aluma-card-profile-name"><strong>{{ fullName }}</strong></span>
                                <br>
                                {{ userName }}
                                <br>
                                {{ email }}
                                <br>
                            </div>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name"><strong>Bio</strong><button class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil" v-on:click="toggleEditBio()"></i></button></span>
                            <hr>
                            <div id="orignalBio" v-show="originalBio">{{ bio }}</div>
                            <div class="" v-show="showBioForm">
                                <form class="form-group" @submit.prevent="editBio">
                                    <label><b>Edit Bio</b></label>
                                    <textarea class="form-control mb-3" :placeholder="bio" v-model="newBio"></textarea>
                                    <center>
                                        <button class="btn btn-dark" type="submit" style="margin-right: 30px">Edit</button>
                                        <button class="btn btn-dark" v-on:click="toggleEditBio()">Close</button>
                                    </center>
                                </form>
                            </div>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name"><strong>Experience</strong><button class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil" v-on:click="toggleEditExp()"></i></button></span><hr>
                            <div class="" v-show="originalExp">
                                <div class="" v-for="(index) in numberOfExp" :key="index">
                                    <p>
                                        <strong>{{ companies[index-1] }}</strong>
                                        <br>
                                        {{ durations[index-1] }}
                                        <br>
                                        {{ positions[index-1] }}
                                        <br>
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name">Bookmarks</span><hr>
                            <p>Bookmarks here</p>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name">Interests</span><hr>
                            <p>Interests Here</p>
                        </div>                    
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
import Navbar from './Navbar.vue'
import MobileNavbar from './MobileNavbar.vue'
import jwtDecode from 'jwt-decode'
import axios from 'axios'
// import $ from 'jquery'
export default {
    data () {
        return {
            fullName: jwtDecode(localStorage.usertoken).identity.full_name,
            userName: jwtDecode(localStorage.usertoken).identity.user_name,
            email: jwtDecode(localStorage.usertoken).identity.email,
            // Bio stuff
            bio: '',
            newBio: '',
            showBioForm: false,
            originalBio: true,

            // Experience stuff
            companies: [],
            durations: [],
            positions: [],
            numberOfExp: 0,
            originalExp: true
        }
    },
    components: {
        'navbar': Navbar,
        'mbnav': MobileNavbar,

    },
    name: 'Profile',
    methods:{
        toggleEditBio () {
            this.originalBio = !this.originalBio
            this.showBioForm = !this.showBioForm
        },
        getBio () {
            const payload ={
                user : this.userName
            }
            const path = "http://127.0.0.1:5000/getbio";

            axios.post(path,payload).then((res) => {
                this.bio = res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getExp () {
            const payload ={
                user : this.userName
            }
            const path = "http://127.0.0.1:5000/getwork";

            axios.post(path,payload).then((res) => {
                this.companies = res.data["companies"]
                this.durations = res.data["durations"]
                this.positions = res.data["positions"]
                this.numberOfExp = this.companies.length
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        }, 
        editBio () {
            if (this.newBio.length === 0) {
                this.newBio = this.bio
            }
            var payload = {
                user : this.userName,
                bio : this.newBio
            }
            const path = "http://127.0.0.1:5000/editbio";

            axios.post(path,payload).then((res) => {
                this.bio = res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
            this.showBioForm = false
            this.originalBio = true
        }
    },
    mounted() {
        this.getBio();
        this.getExp();
    }
}
</script>
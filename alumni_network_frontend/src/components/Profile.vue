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
                            <span class="aluma-card-profile-name"><strong>Bio</strong><button class="btn btn-outline-dark border-0 float-right" v-on:click="toggleEditBio"><i class="fa fa-pencil"></i></button></span>
                            <hr>
                            <div id="orignalBio" v-show="originalBio">{{ bio }}</div>
                            <div class="" v-show="showBioForm">
                                <form class="form-group" @submit.prevent="editBio">
                                    <label><b>Edit Bio</b></label>
                                    <textarea class="form-control mb-3" :placeholder="bio" v-model="newBio"></textarea>
                                    <center>
                                        <button class="btn btn-dark" type="submit" style="margin-right: 30px">Edit</button>
                                        <button class="btn btn-dark" v-on:click="toggleEditBio">Close</button>
                                    </center>
                                </form>
                            </div>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name"><strong>Experience</strong><button class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil"></i></button></span><hr>
                            <div class="">
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
                            <span class="aluma-card-profile-name"><strong>Interests</strong><button class="btn btn-outline-dark border-0 float-right" v-on:click="toggleEditInterests"><i class="fa fa-pencil"></i></button></span><hr>
                            <div class="" v-show="originalInterests">
                                <span><strong>Country of Interest: </strong> {{ country }} </span>
                                <br>
                                <span><strong>Subject of Interest: </strong> {{ subject }} </span>
                                <br>
                                <span><strong>Specialisation: </strong> {{ specialisation }} </span>
                                <br>
                            </div>
                            <div class="" v-show="showInterestsForm">
                                <form class="mb-4" @submit.prevent="editInterests" id="interest">
                                    <span><b>Select Interests</b></span><br><br>
                                    <label>Country of Interest</label>
                                    <select class="form-control mb-3" v-model="newCountry">
                                        <option v-for="c in countries" :key="c._id.$oid" :value="c.name">{{ c.name }}</option>
                                    </select>
                                    <label>Subject of Interest</label>
                                    <select class="form-control mb-3" id="subject" v-model="newSubject">
                                        <option disabled selected>Select Subject</option>
                                        <option v-for="s in subjects" :key="s._id.$oid" :value="s.name">{{ s.name }}</option>
                                    </select>
                                    <label>Select Specialization</label>
                                    <select class="form-control mb-3" v-model="newSpecialisation">
                                        <option disabled selected>Select Subject First</option>
                                        <option v-for="special in specialisations" :key="special._id.$oid" :value="special.name">{{ special.name }}</option>
                                    </select>
                                    <center>
                                        <button class="btn btn-dark" type="submit" style="margin-right: 30px">Edit</button>
                                        <button class="btn btn-dark" v-on:click="toggleEditInterests">Close</button>
                                    </center>
                                </form>
                            </div>
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
import $ from 'jquery'
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

            // Interests stuff
            countries: [],
            subjects: [],
            specialisations: [],
            country: '',
            newCountry: '',
            subject: '',
            newSubject: '',
            specialisation: '',
            newSpecialisation: '',
            showInterestsForm: false,
            originalInterests: true
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
        toggleEditInterests () {
            this.originalInterests = !this.originalInterests
            this.showInterestsForm = !this.showInterestsForm
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
        getcountries(){
            const payload={
                parent: 'Country'
            }
            const path="http://127.0.0.1:5000/getchildcategories"
            axios.post(path,payload).then((res) => {
                this.countries=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getsubjects(){
            const payload={
                parent: 'Subject'
            }
            const path="http://127.0.0.1:5000/getchildcategories"
            axios.post(path,payload).then((res) => {
                this.subjects=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getspecialization(subject){
            const payload={
                parent: subject
            }
            const path="http://127.0.0.1:5000/getgrandchildcategories"
            axios.post(path,payload).then((res) => {
                this.specialisations=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getInterests () {
            const payload ={
                user : this.userName
            }
            const path = "http://127.0.0.1:5000/getinterest";

            axios.post(path,payload).then((res) => {
                this.country = res.data[0]
                this.subject = res.data[1]
                this.specialisation = res.data[2]
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        editInterests () {
            if (this.newCountry.length === 0) {
                this.newCountry = this.country
            }
            if (this.newSubject.length === 0) {
                this.newSubject = this.subject
            }
            if (this.newSpecialisation.length == 0) {
                this.newSpecialisation = this.specialisation
            }

            var newInterests = [this.newCountry, this.newSubject, this.newSpecialisation]

            const payload = {
                user : this.userName,
                interest : newInterests
            }
            const path = "http://127.0.0.1:5000/editinterest";

            axios.post(path,payload).then((res) => {
                this.country = res.data[0]
                this.subject = res.data[1]
                this.specialisation = res.data[2]
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
            this.showInterestsForm = false
            this.originalInterests = true
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
        this.getcountries();
        this.getsubjects();
        this.getInterests();
        $('#subject').on('change', (evt) => {
            this.getspecialization($(evt.target).val());
        });
    }
}
</script>
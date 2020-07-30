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
                <div class="col-lg-4 sm-auto md-auto offset-lg-4 p-3">
                    <div class="aluma-card p-3">
                    <div class="alert alert-info">Please Complete your Profile for better user expirience</div>
                    <form class="form-group" @submit.prevent="addbio" id="bio">
                        <label><b>Add Bio</b></label>
                        <textarea class="form-control mb-3" placeholder="Bio" v-model="bio"></textarea>
                        <button class="btn btn-dark" type="submit">Add</button>
                    </form>
                    <hr>
                    <form @submit.prevent="addexp" class="mb-4">    
                        <span><b>Add Work Experience</b></span><br><br>
                        <input type="text" placeholder="Position" class="form-control mb-3" v-model="position">
                        <input type="text" placeholder="Place Of Work" class="form-control mb-3" v-model="place">
                        <input type="text" placeholder="Start Date" class="form-control mb-3" id="startdate" v-model="start" onfocus="this.type='date'">
                        <input type="text" placeholder="End Date" class="form-control mb-3" id="enddate" v-model="end" onfocus="this.type='date'">
                        <input type="checkbox"  id="check" class="form-check-input ml-1"><label class="ml-4">I currently work here.</label><br>
                        <button class="btn btn-dark" type="submit">Add</button>
                    </form>
                    <hr>
                    <form class="mb-4" @submit.prevent="addedu">
                        <span><b>Add Education</b></span><br><br>
                        <input type="text" placeholder="Degree/Specialization" class="form-control mb-3" v-model="degree">
                        <input type="text" placeholder="Institution" class="form-control mb-3" v-model="institute">
                        <input type="text" placeholder="Start Date" class="form-control mb-3" id="estartdate" v-model="estart" onfocus="this.type='date'">
                        <input type="text" placeholder="End Date" class="form-control mb-3" id="eenddate" v-model="eend" onfocus="this.type='date'">
                        <input type="checkbox"  id="echeck" class="form-check-input ml-1"><label class="ml-4">I currently study here.</label><br>
                        <button class="btn btn-dark" type="submit">Add</button>
                    </form>
                    <hr>
                    <form class="mb-4" @submit.prevent="addinterest" id="interest">
                        <label><b>Countries of Interest</b></label>
                        <div class="table-responsive">
                            <table class="table borderless">
                            <tr><th v-for="country in countries" :key="country._id.$oid"><tr><input type="checkbox" :id="country._id.$oid" :value="country.name" @change="addtoarray(country._id.$oid)"></tr><tr>{{country.name}}</tr></th></tr>
                            </table>
                        </div>
                        <hr>
                        <label><b>Subjects of Interest</b></label>
                        <div class="table-responsive">
                            <table class="table borderless">
                            <tr><th v-for="subject in subjects" :key="subject._id.$oid"><tr><input type="checkbox" :id="subject._id.$oid" :value="subject.name" @change="addtoarray(subject._id.$oid)"></tr><tr>{{subject.name}}</tr></th></tr>
                            </table>
                        </div><hr>
                        <label>Select Specialization</label>
                        <div class="table-responsive">
                            <table class="table borderless">
                            <tr><th v-for="special in specializations" :key="special._id.$oid"><tr><input type="checkbox" :value="special.name" :id="special._id.$oid" @change="addtoarray(special._id.$oid)"></tr><tr>{{special.name}}</tr></th></tr>
                            </table>
                        </div><hr>
                        <button class="btn btn-dark" type="submit">Save</button>
                    </form>
                    <button class="btn btn-dark" @click="complete" style="display:none" id="complete">Complete</button>
                    </div>
                </div>   
            </div>
        </div>
    </div>
</template>
<script>
import MobileNavbar from './MobileNavbar.vue'
import jwtDecode from 'jwt-decode';
import $ from 'jquery'
import axios from 'axios';
export default {
    components: {
        'mbnav': MobileNavbar,
    },
    data() {
        return {
            position: '',
            place:'',
            start:'',
            end:'',
            bio:'',
            degree:'',
            institute:'',
            estart:'',
            eend:'',
            interests:[],
            countries: [],
            subjects: [],
            specializations: [],
            selectedinterest:[],
        }
    },
    name: 'CompleteProfile',
    methods: {
        logout() {
            localStorage.clear();
            this.$router.push({ name: 'Home' });
        },
        addexp(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                position:this.position,
                place:this.place,
                start:this.start,
                end:this.end,
                user:user_decode.identity.user_name
            };
            const path="http://127.0.0.1:5000/addwork";
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                if(res.data=="200"){
                    alert("Expirience Added");
                    this.position="";
                    this.place="";
                    this.start="";
                    this.end="";
                    $("#enddate").fadeIn('slow');
                    document.getElementById('enddate').type = 'text';
                    document.getElementById('startdate').type = 'text';
                    $('#check').prop('checked', false);
                }
                else
                {
                    alert('Failed');
                }
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        addedu(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                degree:this.degree,
                institute:this.institute,
                start:this.estart,
                end:this.eend,
                user:user_decode.identity.user_name
            };
            const path="http://127.0.0.1:5000/addedu";
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                if(res.data=="200"){
                    alert("Education Added");
                    this.degree="";
                    this.institute="";
                    this.estart="";
                    this.eend="";
                     $("#eenddate").fadeIn('slow');
                     document.getElementById('eenddate').type = 'text';
                     document.getElementById('estartdate').type = 'text';
                    $('#echeck').prop('checked', false);
                }
                else
                {
                    alert('Failed');
                }
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },

        addbio() {
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user);
            const payload={
                bio:this.bio,
                user:user_decode.identity.user_name
            };
            const path="http://127.0.0.1:5000/addbio";
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                if(res.data=="200"){
                    alert("Bio Added");
                }
                else
                {
                    alert('Failed');
                }
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
            $('#bio').fadeOut('slow');
        },
        addinterest() {
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user);
            const payload={
            interest:this.selectedinterest,
            user:user_decode.identity.user_name
            };
            console.log(payload)
            const path="http://127.0.0.1:5000/addinterests";
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                if(res.data=="200"){
                    alert("Interest Added");
                    $('#interest').fadeOut('slow');
                    $('#complete').fadeIn('slow');
                }
                else
                {
                    alert('Failed');
                }
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
                console.log(res.data);
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
                console.log(res.data);
                this.subjects=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getspecialization(){
            const payload={}
            const path="http://127.0.0.1:5000/getgrandchildcategories"
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                this.specializations=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        complete() {
            this.$router.push({ name: 'Feed' });
        },
        addtoarray(id){
            id="#"+id;
            if($(id).prop("checked")==true){
                this.selectedinterest.push($(id).val());
                console.log(this.selectedinterest);
            }
            else{
                this.selectedinterest = this.selectedinterest.filter(item => item !== $(id).val())
                console.log(this.selectedinterest)
            }
      }
    },
    mounted() {
        $("#check").change(function() {
            if(this.checked) {
                $("#enddate").fadeOut('slow');
                document.getElementById('enddate').type = 'text';
                $("#enddate").val("Present")[0].dispatchEvent(new Event('input'));
            }
            else{
                $("#enddate").fadeIn('slow');
                $("#enddate").val("")[0].dispatchEvent(new Event('input'));
            }
        });
        $("#echeck").change(function() {
            if(this.checked) {
                $("#eenddate").fadeOut('slow');
                document.getElementById('eenddate').type = 'text';
                $("#eenddate").val("Present")[0].dispatchEvent(new Event('input'));
            }
            else{
                $("#eenddate").fadeIn('slow');
                $("#eenddate").val("")[0].dispatchEvent(new Event('input'));
            }
        });
        $('#subject').on('change', (evt) => {
            this.getspecialization($(evt.target).val());
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
      });
      
        this.getcountries();
        this.getsubjects();
        this.getspecialization();
    }
}
</script>
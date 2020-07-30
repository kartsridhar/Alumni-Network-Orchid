<template>
    <div>
        <navbar/>
        <mbnav/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div v-for="category in categories" :key="category._id.$oid">
                        <div class="aluma-card">
                            <span @click="show('#'+category._id.$oid)" style="cursor:pointer"><b>{{category.name}}</b></span><br>
                            <div :id="category._id.$oid" style="display:none;" class="pt-4 pl-4 pr-4">
                                <div class="table-responsive">
                                    <table class="table table-borderless">
                                        <tr class="border-bottom" v-for="child in children" :key="child._id.$oid">
                                            <td v-if="child.parent===category.name"><span @click="go(child.name)" style="cursor:pointer">{{child.name}}</span>
                                            <td v-if="child.parent===category.name" class="text-right">
                                                <button class="btn btn-white" @click="changeClass('#'+child._id.$oid+'int',child.name)">
                                                    <i v-if="interests.includes(child.name)" :id="child._id.$oid+'int'" class="fa fa-check"></i>
                                                    <i v-else :id="child._id.$oid+'int'" class="fa fa-plus"></i>
                                                </button>
                                            </td>
                                        </tr>
                                    </table>
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
import Navbar from './Navbar.vue'
import MobileNavbar from './MobileNavbar.vue'
import jwtDecode from 'jwt-decode';
import $ from 'jquery';
import axios from 'axios';
export default {
    components: {
        'navbar': Navbar,
        'mbnav': MobileNavbar,
    },
    data(){
        return{
            categories:[],
            children:[],
            interests:[],
        }
    },
    name: 'Discover',
    methods: {
        getcategories(){
             const path="http://127.0.0.1:5000/getcategories"
             axios.get(path).then((res) => {
                 console.log(res.data)
                 this.categories=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getchild(){
             const path="http://127.0.0.1:5000/getchildcategories"
             const payload={
             }
             axios.post(path,payload).then((res) => {
                 console.log(res.data)
                 this.children=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        show(id){
            if($(id).is(":visible")){
                $(id).slideUp('slow');
            }
            else{
                $(id).slideDown('slow');
            }
        },
        go(n){
            localStorage.setItem('category', n);
            this.$router.push({name:'Category'})
        },
        changeClass(id,id1)
        {
            if($(id).hasClass("fa fa-plus"))
            {
                $(id).removeClass("fa fa-plus",{duration:500});
                $(id).addClass("fa fa-check",{duration:500});
                this.addinterest(id1);
            }
            else if($(id).hasClass("fa fa-check"))
            {
                $(id).removeClass("fa fa-check",{duration:500});
                $(id).addClass("fa fa-plus",{duration:500});
                this.delinterest(id1);
            }
        },
        addinterest(n){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                interest:n,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/addinterest"
            axios.post(path,payload).then((res) => {
                 console.log(res.data)
                 this.getinterests()
                 
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        delinterest(n){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                interest:n,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/removeinterest"
            axios.post(path,payload).then((res) => {
                 console.log(res.data)
                 this.getinterests()
                 
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getinterests(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/getinterest"
            axios.post(path,payload).then((res) => {
                this.interests=res.data         
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
    },
    mounted(){
        this.getcategories();
        this.getchild();
        this.getinterests();
    }
}
</script>
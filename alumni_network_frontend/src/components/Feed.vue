<template>
    <div>
        <navbar/>
        <mbnav/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="container-fluid pt-1 pb-3">
                        <div align="center" id="newpost" class="sticky-top p-3" style="display:none"><button class="btn btn-outline-light btn-dark" @click="buttongetpost"><i class="fa fa-arrow-up"></i> New Posts</button></div>
                        <div class="aluma-card">
                            <span id="initPost" class="pointer"><i class="fa fa-pencil-square-o"></i>&emsp;Start A Post</span>
                            <div id="writePost" style="display:none">
                                <span id="postHead">Write something...</span><hr>
                                <form class="p-1" @submit.prevent="addpost">
                                    <input class="form-control mb-3" id="name" type="text" placeholder="Title" v-model="title">
                                    <textarea class="form-control mb-3" id="username" placeholder="Content" v-model="content"></textarea>
                                    <div class="form-row mb-3">
                                        <div class="col">
                                            <label>Tag 1</label>
                                            <select class="form-control" v-model="tag1">
                                                <option v-for="country in countries" :key="country._id.$oid" :value="country.name">{{country.name}}</option>
                                            </select>
                                        </div>
                                        <div class="col">
                                            <label>Tag 2</label>
                                            <select class="form-control" v-model="tag2">
                                                <option v-for="subject in subjects" :key="subject._id.$oid" :value="subject.name">{{subject.name}}</option>
                                                <option v-for="exam in exams" :key="exam._id.$oid" :value="exam.name">{{exam.name}}</option>
                                            </select>
                                        </div>
                                        <div class="col">
                                            <label>Tag 3</label>
                                            <select class="form-control" v-model="tag3">
                                                <option v-for="special in specializations" :key="special._id.$oid" :value="special.name">{{special.name}}</option>
                                            </select>
                                        </div>                                    
                                    </div>
                                    <button class="btn btn-dark" type="submit">Post</button>&emsp;&emsp;
                                    <span class="btn btn-outline-dark" id="closePost">Cancel</span>
                                </form>
                            </div>
                        </div>
                        <div class="aluma-card-post" v-for="post in posts" :key="post._id.$oid">
                            <span class="aluma-card-post-title">{{post.user}}</span><hr>
                            <div class="aluma-card-post-content">
                                {{post.title}}<br>
                                {{post.content}}
                            </div>
                            <div :id="post._id.$oid+'cmnt'"  class="aluma-card-post-comment">
                                    <form class="" @submit.prevent="addcomment(post._id.$oid)">
                                        <div class="form-row">
                                            <div class="col-lg-10 sm-auto md-auto mb-2"><input class="form-control" type="text" placeholder="comment" v-model="comment"></div>
                                            <div class="col-lg-2 sm-auto md-auto mb-2"><span @click="toggleComment('#'+post._id.$oid+'cmnt','#'+post._id.$oid+'postFooter')" class="btn btn-outline-dark float-right">&times;</span><button class="btn btn-dark float-right mr-2" type="submit"><i class="fa fa-paper-plane-o"></i></button></div>
                                        </div>
                                    </form>
                                    <ul class="list-group">
                                        <li class="list-group-item" v-for="item in post.comment" :key="item.timestamp">
                                            <span style="color:grey;">{{ item.user }}</span><br>
                                            <span style="font-size:small;" class="ml-3">{{ item.comment }}</span>   
                                        </li>
                                    </ul>
                             </div>
                             <div class="aluma-card-post-footer" align="left" :id="post._id.$oid+'postFooter'">
                                <button @click="changeClass('#'+post._id.$oid+'lk')"><i :id="post._id.$oid+'lk'" class="fa fa-thumbs-o-up"></i></button>
                                <button @click="changeClass('#'+post._id.$oid+'bk')"><i :id="post._id.$oid+'bk'" class="fa fa-bookmark-o"></i></button>
                                <button @click="toggleComment('#'+post._id.$oid+'cmnt','#'+post._id.$oid+'postFooter')"><i class="fa fa-comment-o"></i></button>
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
    name: 'Feed',
    data() {
        return {
            title:"",
            content:"",
            tag1:"",
            tag2:"",
            tag3:"",
            countries: [],
            subjects: [],
            exams:[],
            specializations: [],
            posts:[],
            count:0,
            prevcount:0,
            comment:""
        }
    },
    methods: {
        changeClass:function changeClass(id)
        {
            if($(id).hasClass("fa fa-thumbs-o-up"))
            {
                $(id).removeClass("fa fa-thumbs-o-up",{duration:500});
                $(id).addClass("fa fa-thumbs-up",{duration:500});
            }
            else if($(id).hasClass("fa fa-thumbs-up"))
            {
                $(id).removeClass("fa fa-thumbs-up",{duration:500});
                $(id).addClass("fa fa-thumbs-o-up",{duration:500});
            }
            else if($(id).hasClass("fa-bookmark-o"))
            {
                $(id).removeClass("fa-bookmark-o",{duration:500});
                $(id).addClass("fa-bookmark",{duration:500});
            }
            else if($(id).hasClass("fa-bookmark"))
            {
                $(id).removeClass("fa-bookmark",{duration:500});
                $(id).addClass("fa-bookmark-o",{duration:500});
            }
        },
        toggleComment:function toggleComment(id,id1)
        {
            if($(id).css('display')=='none')
            {
                $(id).slideDown('slow');
                $(id1).slideUp('slow');
            }
            else
            {
                $(id).slideUp('slow');
                $(id1).slideDown('slow');
            }
        },
        getcountries(){
            const payload={
                parent: "Country"
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
                parent: 'Subject',
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
        getexams(){
            const payload={
                parent: 'Exam',
            }
            const path="http://127.0.0.1:5000/getchildcategories"
            axios.post(path,payload).then((res) => {
                
                this.exams=res.data;
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
                
                this.specializations=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        addpost(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            var arr=[this.tag1,this.tag2,this.tag3]
            const payload ={
                title:this.title,
                content:this.content,
                tags:arr,
                user:user_decode.identity.user_name,
                comment:[],
                timestamp:Math.round(+new Date()/1000)
            }
            const path="http://127.0.0.1:5000/createpost"
            axios.post(path,payload).then((res) => {
                if(res.data=="200"){
                    alert("Post Added");
                    this.title="";
                    this.content="";
                    this.tag1="";
                    this.tag2="";
                    this.tag3="";
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
        addcomment(id){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            var payload={
               comment:this.comment,
               user: user_decode.identity.user_name,
               timestamp:Math.round(+new Date()/1000),
               post:id
            }
            const path="http://127.0.0.1:5000/addcomment"
            axios.post(path,payload).then((res) => {
                if(res.data=="200"){
                    alert("Comment Added");
                    this.comment="";
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
        getpost(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload ={
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/getpost"
            axios.post(path,payload).then((res) => {
                    this.posts=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getpostcount(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload ={
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/getpostcount"
            axios.post(path,payload).then((res) => {
                    this.count=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        buttongetpost(){
            this.getpost();
            $("html, body").animate({ scrollTop: 0 }, "slow");
        }
    },
    mounted() {
        $(function () {
            $("#initPost").on("click",function(){
                $("#writePost").slideDown('slow');
                $("#initPost").fadeOut('slow');
                $("postHead").fadeIn('slow');
            })
            $("#closePost").on("click",function(){
                $("#writePost").slideUp('slow');
                $("#initPost").fadeIn('slow');
            })
        })
        this.getcountries();
        this.getsubjects();
        this.getexams();
        this.getspecialization();
        this.getpost();
        setInterval(() => {
            //$("#newpost").fadeIn('slow').delay(5000).fadeOut('slow');
            this.getpostcount()
            if(this.prevcount<this.count){
                console.log(this.prevcount)
                this.prevcount=this.count;
                $("#newpost").fadeIn('slow').delay(3000).fadeOut('slow');
            }
        },60000);
    },
}
</script>
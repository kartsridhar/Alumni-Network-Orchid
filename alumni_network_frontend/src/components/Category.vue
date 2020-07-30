<template>
    <div>
        <navbar/>
        <mbnav/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="pb-2 mt-2 text-center">
                    <h1>{{category}}</h1>
                    </div>
                        <div class="aluma-card-post" v-for="post in posts" :key="post._id.$oid" :id="post._id.$oid">
                            <span class="aluma-card-post-title"><i class="fa fa-user-circle-o pl-2" style="font-size:30px;"></i> {{post.user}}</span>
                            <div class="aluma-card-post-content mt-3">
                                {{post.title}}<br>
                                {{post.content}}<br>
                            </div>
                            <div :id="post._id.$oid+'cmnt'"  class="aluma-card-post-comment">
                                    <form class="" @submit.prevent="addcomment(post._id.$oid)">
                                        <div class="form-row">
                                            <div class="col-lg-10 sm-auto md-auto mb-2"><input class="form-control" type="text" placeholder="comment" v-model="comment"></div>
                                            <div class="col-lg-2 sm-auto md-auto mb-2"><span @click="toggleComment('#'+post._id.$oid+'cmnt','#'+post._id.$oid+'postFooter')" class="btn btn-outline-dark float-right">&times;</span><button class="btn btn-dark float-right mr-2" type="submit"><i class="fa fa-paper-plane-o"></i></button></div>
                                        </div>
                                    </form>
                                    <div class="p-2">
                                        <p v-for="item in post.comment" :key="item.timestamp">
                                            <span style="color:grey;font-size:small;">@{{ item.user }}</span><br>
                                            <span style="font-size:large;" class="ml-2">{{ item.comment }}</span>   
                                        </p>
                                </div>
                             </div>
                             <div class="aluma-card-post-footer" align="left" :id="post._id.$oid+'postFooter'">
                                <button @click="changeClass('#'+post._id.$oid+'lk',post._id.$oid)">
                                    <i v-if="post.likers.includes(current_user)"  :id="post._id.$oid+'lk'" class="fa fa-thumbs-up"></i>
                                    <i v-else :id="post._id.$oid+'lk'" class="fa fa-thumbs-o-up"></i>
                                    <span style="color:grey; font-size:medium" class="ml-2">{{post.likes}}</span>
                                </button>
                                
                                <button @click="toggleComment('#'+post._id.$oid+'cmnt','#'+post._id.$oid+'postFooter')">
                                    <i class="fa fa-comment-o"></i>
                                    <span style="color:grey; font-size:medium" class="ml-2">{{post.comment.length}}</span>
                                </button>
                                <button @click="changeClass('#'+post._id.$oid+'bk',post._id.$oid)" class="float-right">
                                        <i v-if="bookmarks.includes(post._id.$oid)"  :id="post._id.$oid+'bk'" class="fa fa-bookmark"></i>
                                        <i v-else :id="post._id.$oid+'bk'" class="fa fa-bookmark-o"></i>
                                </button>
                             </div>
                        </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
//import $route from '../router'
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
            category:"",
            posts:[],
            comment:"",
            current_user:"",
            bookmarks:[]
        }
    },
    name: 'Category',
    methods: {
        changeClass:function changeClass(id,id1)
        {
            if($(id).hasClass("fa fa-thumbs-o-up"))
            {
                $(id).removeClass("fa fa-thumbs-o-up",{duration:500});
                $(id).addClass("fa fa-thumbs-up",{duration:500});
                this.addlike(id1)
            }
            else if($(id).hasClass("fa fa-thumbs-up"))
            {
                $(id).removeClass("fa fa-thumbs-up",{duration:500});
                $(id).addClass("fa fa-thumbs-o-up",{duration:500});
                this.dellike
            }
            else if($(id).hasClass("fa-bookmark-o"))
            {
                $(id).removeClass("fa-bookmark-o",{duration:500});
                $(id).addClass("fa-bookmark",{duration:500});
                this.addbookmark(id1)
            }
            else if($(id).hasClass("fa-bookmark"))
            {
                $(id).removeClass("fa-bookmark",{duration:500});
                $(id).addClass("fa-bookmark-o",{duration:500});
                this.removebookmark(id1)
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
        getpost(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            this.current_user=user_decode.identity.user_name
            const payload ={
                cat:this.category
            }
            const path="http://127.0.0.1:5000/getcategorypost"
            axios.post(path,payload).then((res) => {
                    this.posts=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        addlike(id){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                post_id:id,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/addlike"
            axios.post(path,payload).then((res) => {
                console.log(res.data)
                this.getpost()
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        dellike(id){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                post_id:id,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/removelike"
            axios.post(path,payload).then((res) => {
                console.log(res.data)
                this.getpost()
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
                    this.getpost();

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
        addbookmark(id){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                post_id:id,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/addbookmark"
            axios.post(path,payload).then((res) => {
                console.log(res.data)
                this.getbookmarks()
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        removebookmark(id){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                post_id:id,
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/removebookmark"
            axios.post(path,payload).then((res) => {
                console.log(res.data)
                this.getbookmarks()
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getbookmarks(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            const payload={
                user:user_decode.identity.user_name
            }
            const path="http://127.0.0.1:5000/getbookmark"
            axios.post(path,payload).then((res) => {
                console.log(res.data)
                this.bookmarks=res.data.bookmarks
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
    },
    created(){
        this.category=localStorage.category;
        this.getpost()
        this.getbookmarks()
    },
    mounted(){
    }
}
</script>
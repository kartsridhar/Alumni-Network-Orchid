<template>
    <div>
        <navbar/>
        <mbnav/>
        <div class="container-fluid pb-3">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="pt-1" id="feed">
                        <div align="center" id="newpost" class="sticky-top p-3" style="display:none"><button class="btn btn-outline-light btn-dark" @click="buttongetpost"><i class="fa fa-arrow-up"></i> New Posts</button></div>
                        <div class="aluma-card">
                            <span id="initPost" class="pointer"><i class="fa fa-pencil-square-o"></i>&emsp;Start A Post</span>
                            <div id="writePost" style="display:none">
                                <span id="postHead">Write something...</span><hr>
                                <form class="p-1" @submit.prevent="addpost">
                                    <input class="form-control mb-3" id="name" type="text" placeholder="Title" v-model="title">
                                    <textarea class="form-control mb-3" id="username" placeholder="Content" v-model="content"></textarea>
                                    <div class="dropdown">
                                        <span class="dropdown-toggle form-control mb-3" type="button" id="sampleDropdownMenu" data-toggle="dropdown">Tags</span>
                                        <div class="dropdown-menu" style="height:300px; overflow-y:scroll;">
                                            <span class="dropdown-item"  v-for="country in countries" :key="country._id.$oid">
                                                <input type="checkbox" :id="country._id.$oid" :value="country.name" @change="addtoarray(country._id.$oid)"> {{country.name}}
                                            </span>
                                            <span class="dropdown-item" v-for="special in specializations" :key="special._id.$oid" >
                                                <input type="checkbox" :id="special._id.$oid" :value="special.name" @change="addtoarray(special._id.$oid)"> {{special.name}}
                                            </span>
                                            <span class="dropdown-item"  v-for="subject in subjects" :key="subject._id.$oid">
                                                <input type="checkbox" :id="subject._id.$oid" :value="subject.name" @change="addtoarray(subject._id.$oid)"> {{subject.name}}
                                            </span>
                                            <span class="dropdown-item"  v-for="exam in exams" :key="exam._id.$oid">
                                                <input type="checkbox" :id="exam._id.$oid" :value="exam.name" @change="addtoarray(exam._id.$oid)"> {{exam.name}}
                                            </span>
                                        </div>
                                    </div>
                                    <div id="tags" class="alert alert-info mb-3" style="display:none"></div>
                                    <button class="btn btn-dark" type="submit">Post</button>&emsp;&emsp;
                                    <span class="btn btn-outline-dark" id="closePost">Cancel</span>
                                </form>
                            </div>
                        </div>
                        <div class="aluma-card-post" v-for="post in posts" :key="post._id.$oid" :id="post._id.$oid">
                            <span class="aluma-card-post-title" @click="gotouser(post.user)"><i class="fa fa-user-circle-o pl-2" style="font-size:30px;"></i> {{post.user}}</span>
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
            tags:[],
            countries: [],
            subjects: [],
            exams:[],
            specializations: [],
            posts:[],
            count:0,
            prevcount:0,
            comment:"",
            current_user:"",
            bookmarks:[]
        }
    },
    methods: {
        changeClass:function changeClass(id,id1)
        {
            if($(id).hasClass("fa fa-thumbs-o-up"))
            {
                $(id).removeClass("fa fa-thumbs-o-up",{duration:500});
                $(id).addClass("fa fa-thumbs-up",{duration:500});
                this.addlike(id1);
            }
            else if($(id).hasClass("fa fa-thumbs-up"))
            {
                $(id).removeClass("fa fa-thumbs-up",{duration:500});
                $(id).addClass("fa fa-thumbs-o-up",{duration:500});
                this.dellike(id1);
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
            var arr=this.tags
            const payload ={
                title:this.title,
                content:this.content,
                tags:arr,
                user:user_decode.identity.user_name,
                comment:[],
                likes:0,
                likers:[],
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
                    window.location.reload()
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
        getpost(){
            var user=localStorage.usertoken;
            var user_decode=jwtDecode(user)
            this.current_user=user_decode.identity.user_name
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
        },
        addtoarray(id){
            id="#"+id;
            if($(id).prop("checked")==true){
                
            if(this.tags.length<3)
            {
                this.tags.push($(id).val());
                console.log(this.tags);
                $("#tags").text(this.tags)
                $("#tags").fadeIn();
            }
            else{
                alert('Only 3 tags can be added');
                 $(id).prop("checked",false);
            }
            }
            else{
                this.tags = this.tags.filter(item => item !== $(id).val())
                console.log(this.tags)
                $("#tags").text(this.tags.toString())
                $("#tags").fadeIn();
            }
            
      },
      gotouser(username){
        const current=jwtDecode(localStorage.usertoken).identity.user_name
        if(username==current)
        {
            this.$router.push({name:'Profile'})    
        }
        else{
            localStorage.setItem('uservisit', username);
            this.$router.push({name:'User'})
        }
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
        this.getbookmarks();
        setInterval(() => {
            //$("#newpost").fadeIn('slow').delay(5000).fadeOut('slow');
            this.getpostcount()
            var height = $(window).scrollTop();
            if(height>500){
                if(this.prevcount<this.count){
                console.log(this.prevcount)
                this.prevcount=this.count;
                $("#newpost").fadeIn('slow').delay(3000).fadeOut('slow');
            }
          }
        },60000);
    },
}
</script>
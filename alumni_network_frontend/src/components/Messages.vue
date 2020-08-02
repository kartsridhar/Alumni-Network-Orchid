<template>
    <div>
        <navbar/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-3 offset-lg-1 bg-nm aluma-card p-0" id="convo">
                    <div style="height:85vh" class="overflow-scroll">
                    <div class="aluma-card-convo-user" v-for="conversation in conversations" :key="conversation._id.$oid">
                        <span @click="chat(conversation.user2)" v-if="conversation.user1==cuser" class="cursor-pointer">{{conversation.user2}}</span>
                        <span @click="chat(conversation.user1)" v-else class="cursor-pointer">{{conversation.user1}}</span>
                    </div>
                    </div>
                </div>
                <div class="col-lg-7 d-lg-block d-none p-0" id="chat">
                    <div class="aluma-card p-0">
                    <div v-if="user2==''" style="height:100%">
                        <div class="p-3 text-center" style="margin-top:30%">
                            <h1>Tap on an user's name to send messages</h1>
                        </div>
                        <div class="pl-3">
                            <i class="fa fa-hand-o-left" style="font-size:50px;"></i>
                        </div>
                    </div>
                    <div v-else>
                        <div class="bg-nm aluma-card-convo-title">
                            {{user2}}
                        </div>
                        <div class="p-3 aluma-convo-body">
                            <div v-for="msg in msgs" :key="msg._id.$oid"> 
                                <div v-if="msg.from==user2" class="float-left user2">
                                    {{msg.message}}
                                </div>
                                <div v-else class="float-right user1">
                                    {{msg.message}}
                                </div><br><br>
                            </div>
                        </div>
                        <div class="bg-nm p-3">
                            <form @submit.prevent="sendmessage">
                                <input type="text" style="width:53vw" class="mr-2" v-model="message">
                                <button type="submit" class="btn btn-dark"><i class="fa fa-arrow-right"></i></button>
                            </form>
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
//import $ from 'jquery'
import jwtDecode from 'jwt-decode'
import $ from 'jquery';
import axios from 'axios'
export default {
    components: {
        'navbar': Navbar,
    },
    name: 'Messages',
    data(){
        return {
            conversations:"",
            user2:"",
            message:"",
            msgs:"",
            cuser:jwtDecode(localStorage.usertoken).identity.user_name,
        }
    },
    methods:{
        getconvo(){
            const payload={
                user:jwtDecode(localStorage.usertoken).identity.user_name
            }
            const path="https://127.0.0.1:5000/getconvo"
            axios.post(path,payload).then((res) => {
                this.conversations=res.data;
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        chat(user){
            this.user2=user;
            this.getmessage();
            if($(window).width()<992){
                $("#chat").removeClass("d-none");
                $("#chat").removeClass("p-0");
                $("#convo").fadeOut("slow");
                $("#chat").fadeIn("slow");
            }
        },
        sendmessage(){
            const payload={
                message:this.message,
                to:this.user2,
                from:jwtDecode(localStorage.usertoken).identity.user_name,
                timestamp:Math.round(+new Date()/1000)
            }
            const path="https://127.0.0.1:5000/sendmessage"
            axios.post(path,payload).then((res) => {
                console.log(res.data);
                this.getmessage();
                this.message=""
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
        getmessage(){
            const payload={
                user2:this.user2,
                user1:jwtDecode(localStorage.usertoken).identity.user_name,
            }
            const path="https://127.0.0.1:5000/getmessages"
            axios.post(path,payload).then((res) => {
                this.msgs=res.data
            })
            .catch((err) => {
                // eslint-disable-next-line
                alert(err);
            });
        },
    },
    mounted(){
        this.getconvo();
        setInterval(()=>{
            this.getmessage();
        }, 3000);
        $( window ).resize(function() {
            if($(window).width()>992)
            {
                $("#chat").addClass("d-none");
                $("#chat").addClass("p-0");
                $("#convo").fadeIn("slow");
                $("#chat").fadeIn("slow");
            }
            });
    }
}
</script>
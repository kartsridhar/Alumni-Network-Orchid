<template>
    <div>
        <navbar/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="container-fluid pdtp-1">
                        <div class="aluma-card">
                            <span id="initPost" class="pointer"><i class="fa fa-pencil-square-o"></i>&emsp;Start A Post</span>
                            <div id="writePost" style="display:none">
                                <span id="postHead">Write something...</span><hr>
                                <form class="p-2">
                                    <input class="form-control mb-3" id="name" type="text" placeholder="Title">
                                    <textarea class="form-control mb-3" id="username" placeholder="Content"></textarea>
                                    <input type="email" id="defaultSignupFormEmail" class="form-control mb-3" placeholder="category">
                                    <button class="btn btn-dark" type="submit">Post</button>&emsp;&emsp;
                                    <span class="btn btn-outline-dark" id="closePost">Cancel</span>
                                </form>
                            </div>
                        </div>
                        <div class="aluma-card-post">
                            <div class="aluma-card-post-content">
                             Posts accn to category here
                            </div>
                             <div class="aluma-card-post-footer" align="left" id="postFooter">
                                <button @click="changeClass('#lk')"><i id="lk" class="fa fa-thumbs-o-up"></i></button>
                                <button @click="changeClass('#bk')"><i id="bk" class="fa fa-bookmark-o"></i></button>
                                <button @click="toggleComment('#cmnt')"><i class="fa fa-comment-o"></i></button>
                             </div>
                             <div id="cmnt" style="display:none;" class="aluma-card-post-comment">
                                    Comments Here
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
import $ from 'jquery'
export default {
    components: {
        'navbar': Navbar,
    },
    name: 'Feed',
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
        toggleComment:function toggleComment(id)
        {
            if($(id).css('display')=='none')
            {
                $(id).slideDown('slow');
            }
            else
            {
                $(id).slideUp('slow');
            }
        },
    },
}
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
</script>
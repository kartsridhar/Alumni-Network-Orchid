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
                                <span class="aluma-card-profile-name">Name of User <button class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil"></i></button></span><br>
                                Work<br>
                                Location<br>
                            </div>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name">Bio<button @click="editBio" id="editBioButton" class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil"></i></button></span><hr>
                            <div id="orignalBio">Bio here</div>
                                <modal name="bioForm" :adaptive="true">
                                    <div class="p-2">
                                        <span class="aluma-card-profile-name">Edit Bio</span><hr>
                                        <form class="p-3">
                                            <textarea class="form-control mb-3" id="newBio" placeholder="Add new bio..."></textarea>
                                            <button class="btn btn-dark" type="submit">Save</button>&emsp;&emsp;
                                            <span class="btn btn-outline-dark" @click="cancel">Cancel</span>
                                        </form>
                                    </div>
                                </modal>
                        </div>
                        <div class="aluma-card" style="margin-top:20px;">
                            <span class="aluma-card-profile-name">Expirience <button class="btn btn-outline-dark border-0 float-right"><i class="fa fa-pencil"></i></button></span><hr>
                            <p>Company Name<br>
                            Duration<br>
                            Position<br></p>
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
import $ from 'jquery'
export default {
    components: {
        'navbar': Navbar,
        'mbnav': MobileNavbar,

    },
    name: 'Profile',
    methods:{
        editBio(){
            const val=$("#orignalBio").text();
            console.log(val)
            $("#newBio").val(val);
            this.$modal.show('bioForm',{valText:val});
        },
        cancel(){
                this.$modal.hide('bioForm');
        }
    }
}
</script>
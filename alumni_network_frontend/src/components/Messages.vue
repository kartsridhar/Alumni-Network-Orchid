<template>
    <div>
        <navbar/>
        <div class="container-fluid">
            <div class="row" id="content">
                <div class="col-lg-6 sm-auto md-auto offset-lg-3">
                    <div class="aluma-card" style="margin-top:20px;" align="center">
                      <h1>Comming Soon.....</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Navbar from './Navbar.vue'
//import $ from 'jquery'
export default {
    components: {
        'navbar': Navbar,
    },
    name: 'Messages',
}
</script>
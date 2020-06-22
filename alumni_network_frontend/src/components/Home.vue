<template>
<div>
    <nav class="navbar navbar-light bg-light" style="background-color:transparent !important;">
  <a class="navbar-brand" href="#">
    <img src="../assets/logo.png" width="70" height="70" alt="">
    Aluma<b>Meet</b>
  </a>
</nav>
    <div class="container-fluid">
        <div class="row" style="padding-top:30px;">
            <div class="col-lg-6 offset-lg-3 sm-auto md-auto">
                <div class="card border-dark text-center">
                    <div class="card-header bg-transparent">
                        <div class="nav nav-tabs nav-justified card-header-tabs">
                            <span class="nav-item nav-link active" id="nav-signup-tab" data-toggle="tab" href="#nav-signup" role="tab" aria-controls="nav-signup" aria-selected="false">Signup</span>
                            <span class="nav-item nav-link" id="nav-login-tab" data-toggle="tab" href="#nav-login" role="tab" aria-controls="nav-login" aria-selected="true">Login</span>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="tab-content" id="nav-tabContent">
                            <div class="tab-pane fade" id="nav-login" role="tabpanel" aria-labelledby="nav-login-tab">
                                <div class="row">
                                    <div class="col-lg-6  sm-auto md-auto">
                                    <div class="contaainer-fluid"><img src="../assets/login.jpg" class="img-fluid rounded"></div>
                                    </div>
                                    <div class="col-lg-6 sm-auto md-auto">
                                        <form class="p-3" style="margin-top:40px">
                                            <input type="email" id="defaultLoginFormEmail" class="form-control mb-4" placeholder="E-mail">
                                            <input type="password" id="defaultLoginFormPassword" class="form-control mb-4" placeholder="Password">
                                            <button class="btn btn-dark btn-block my-4" type="Login">Sign in</button>
                                        </form>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade show active" id="nav-signup" role="tabpanel" aria-labelledby="nav-signup-tab">
                                    <div class="row">
                                        <div class="col-lg-6  sm-auto md-auto">
                                            <div class="contaainer-fluid"><img src="../assets/signup.png" class="img-fluid rounded"></div>
                                        </div>
                                        <div class="col-lg-6 sm-auto md-auto">
                                            <form class="p-2">
                                                <input class="form-control mb-5" id="name" type="text" placeholder="Name">
                                                <input class="form-control mb-5" id="username" type="text" placeholder="Username">
                                                <input type="email" id="defaultSignupFormEmail" class="form-control mb-5" placeholder="E-mail">
                                                <input type="password" id="defaultSignupFormPassword" class="form-control mb-5" placeholder="Password">
                                                <button class="btn btn-dark btn-block my-4" type="submit">Sign in</button>
                                            </form>
                                        </div>
                                    </div>    
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
export default {
    name : 'Home'
}
</script>
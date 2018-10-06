webpackJsonp([2],{

/***/ 406:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SendfeedPageModule", function() { return SendfeedPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__sendfeed__ = __webpack_require__(417);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



//import {FeedbacktitlePage} from '../../pages/feedbacktitle/feedbacktitle';
var SendfeedPageModule = /** @class */ (function () {
    function SendfeedPageModule() {
    }
    SendfeedPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__sendfeed__["a" /* SendfeedPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__sendfeed__["a" /* SendfeedPage */]),
            ],
            exports: [
                __WEBPACK_IMPORTED_MODULE_2__sendfeed__["a" /* SendfeedPage */]
            ],
            entryComponents: [
                __WEBPACK_IMPORTED_MODULE_2__sendfeed__["a" /* SendfeedPage */]
            ]
        })
    ], SendfeedPageModule);
    return SendfeedPageModule;
}());

//# sourceMappingURL=sendfeed.module.js.map

/***/ }),

/***/ 417:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SendfeedPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4_firebase__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__pages_feedbacktitle_feedbacktitle__ = __webpack_require__(250);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};









/**
 * Generated class for the SendfeedPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var SendfeedPage = /** @class */ (function () {
    function SendfeedPage(navCtrl, navParams, afData, uInfo, alertCtrl) {
        var _this = this;
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.afData = afData;
        this.uInfo = uInfo;
        this.alertCtrl = alertCtrl;
        this.mesData = {
            title: "",
            message: ""
        };
        this.oneStar = "ios-star-outline";
        this.twoStar = "ios-star-outline";
        this.threeStar = "ios-star-outline";
        this.fourStar = "ios-star-outline";
        this.fiveStar = "ios-star-outline";
        this.param = this.navParams.get('param1');
        console.log("param", this.param);
        this.usrData = this.uInfo.getUserInfo();
        this.annon = false;
        this.receivePho = this.param.photourl;
        // this.targetedUser = ;
        afData.database.ref('users').child(this.param.id).child('firstname').on("value", function (datasnap) {
            _this.targetFirst = datasnap.val();
        });
        afData.database.ref('users').child(this.param.id).child('lastname').on("value", function (datasnap) {
            _this.targetLast = datasnap.val();
        });
    }
    // lockSlide(){
    //       this.slides.lockSwipeToNext() = true;
    // }
    SendfeedPage.prototype.goToSlide = function (index, type) {
        if (type === void 0) { type = 2; }
        this.slides.lockSwipeToNext(false);
        this.slides.slideTo(index, 500);
        this.slides.lockSwipeToNext(true);
        this.slides.lockSwipeToPrev(true);
        if (type == 1) {
            this.type = 'feedback';
            console.log("chose feedback");
        }
        else if (type == 0) {
            this.type = 'review';
            console.log("chose review");
        }
    };
    SendfeedPage.prototype.goBackSlide = function (index) {
        this.slides.lockSwipeToPrev(false);
        this.slides.slideTo(index, 500);
        this.slides.lockSwipeToNext(true);
    };
    SendfeedPage.prototype.alertControl = function () {
        var _this = this;
        var alertCtrl = this.alertCtrl.create({
            title: "Feedback Sent!",
            buttons: [
                {
                    text: "ok",
                    role: "cancel",
                    handler: function () {
                        console.log("message sent!");
                        _this.navCtrl.pop();
                    }
                }
            ]
        });
        alertCtrl.present();
    };
    //-------------SENDING PUBLIC FEEDBACK--------------------
    SendfeedPage.prototype.ionViewDidLoad = function () {
        this.slides.lockSwipeToNext(true);
        this.slides.lockSwipeToPrev(true);
    };
    SendfeedPage.prototype.sendMessage = function () {
        if (this.type == "feedback") {
            this.sendFeedback();
        }
        else if (this.type == "review") {
            this.sendReview();
        }
    };
    SendfeedPage.prototype.sendReview = function () {
        var _this = this;
        var timeStamp = __WEBPACK_IMPORTED_MODULE_4_firebase__["database"].ServerValue.TIMESTAMP;
        var obj = {
            title: this.mesData.title,
            message: this.mesData.message,
            id: this.usrData.id,
            star: this.curRating,
            firstname: this.usrData.firstname,
            lastname: this.usrData.lastname,
            username: this.usrData.username,
            timeStamp: timeStamp,
        };
        this.afData.database.ref("users").child(this.param.id).child('review').push(obj).then(function (success) {
            var key = success.key;
            _this.afData.database.ref("users").child(_this.param.id).child('review').child(key).update({ key: key });
        });
        //photo urlsd
        this.alertControl();
    };
    SendfeedPage.prototype.sendFeedback = function () {
        var _this = this;
        var timeStamp = __WEBPACK_IMPORTED_MODULE_4_firebase__["database"].ServerValue.TIMESTAMP;
        if (this.annon == false) {
            var obj = {
                type: "publicfeedbacks",
                title: this.mesData.title,
                message: this.mesData.message,
                id: this.usrData.id,
                firstname: this.usrData.firstname,
                lastname: this.usrData.lastname,
                username: this.usrData.username,
                timeStamp: timeStamp,
                photourl: this.usrData.photourl
            };
            this.afData.database.ref("users").child(this.param.id).child('feedbacks').child("publicfeedbacks").push(obj).then(function (success) {
                var key = success.key;
                _this.afData.database.ref("users").child(_this.param.id).child('feedbacks').child("publicfeedbacks").child(key).update({ key: key });
            });
            //photo urlsd
            this.alertControl();
        }
        else if (this.param.allowAnnon && this.annon) {
            var obj2 = {
                type: "anonfeedbacks",
                title: this.mesData.title,
                message: this.mesData.message,
                username: "annonymous",
                id: this.param.id,
                firstname: "annonymous",
                timestamp: timeStamp,
                photourl: "https://firebasestorage.googleapis.com/v0/b/eoko-cc928.appspot.com/o/profiles%2Fdefault_avatar.jpg?alt=media&token=761a4187-2508-44fb-994c-9bd0b6842181"
            };
            this.afData.database.ref("users").child(this.param.id).child('feedbacks').child("anonfeedbacks").push(obj2).then(function (success) {
                var key = success.key;
                _this.afData.database.ref("users").child(_this.param.id).child('feedbacks').child("anonfeedbacks").child(key).update({ key: key });
            });
            this.alertControl();
        }
        else {
            var alertCtrl = this.alertCtrl.create({
                title: "the user does not accept annonymous feedback",
                buttons: [
                    {
                        text: "ok",
                        role: "cancel",
                        handler: function () {
                            console.log("the user does not accept annonymous feedback");
                            _this.navCtrl.pop();
                        }
                    }
                ]
            });
            alertCtrl.present();
        }
    };
    //--------BLOCK USERS----------
    SendfeedPage.prototype.blockUser = function () {
        var _this = this;
        var alert = this.alertCtrl.create({
            title: 'Block this User?',
            message: 'If the blocked user is not annonymous, you can unblock him later by going to your blacklist in the menu',
            buttons: [
                {
                    text: 'No',
                    role: 'cancel',
                    handler: function () {
                        console.log("cancel clicked");
                    }
                },
                {
                    text: 'Yes',
                    handler: function () {
                        console.log("blocked user");
                        var blocked = {};
                        var blockedUsers = {};
                        blockedUsers[_this.param.id] = _this.param.username;
                        blocked[_this.usrData.id] = _this.usrData.username;
                        _this.afData.database.ref('users').child(_this.param.id).child('blocked').update({ blocked: blocked });
                        _this.afData.database.ref('users').child(_this.usrData.id).child("blockedUsers").update(blockedUsers);
                        _this.navCtrl.pop();
                    }
                }
            ]
        });
        // this.uInfo.setUsers();
        alert.present();
    };
    SendfeedPage.prototype.goToTitlePage = function () {
        this.navCtrl.push(__WEBPACK_IMPORTED_MODULE_5__pages_feedbacktitle_feedbacktitle__["a" /* FeedbacktitlePage */], { param: this.param,
            firstName: this.targetFirst,
            lastName: this.targetLast });
    };
    SendfeedPage.prototype.clickStar = function (star) {
        if (star == "one") {
            this.oneStar = "ios-star";
            this.twoStar = "ios-star-outlinee";
            this.threeStar = "ios-star-outlinee";
            this.fourStar = "ios-star-outlinee";
            this.fiveStar = "ios-star-outlinee";
            this.curRating = 1;
        }
        else if (star == "two") {
            this.oneStar = "ios-star";
            this.twoStar = "ios-star";
            this.threeStar = "ios-star-outline";
            this.fourStar = "ios-star-outline";
            this.fiveStar = "ios-star-outline";
            this.curRating = 2;
        }
        else if (star == "three") {
            this.oneStar = "ios-star";
            this.twoStar = "ios-star";
            this.threeStar = "ios-star";
            this.fourStar = "ios-star-outline";
            this.fiveStar = "ios-star-outline";
            this.curRating = 3;
        }
        else if (star == "four") {
            this.oneStar = "ios-star";
            this.twoStar = "ios-star";
            this.threeStar = "ios-star";
            this.fourStar = "ios-star";
            this.fiveStar = "ios-star-outline";
            this.curRating = 4;
        }
        else if (star == "five") {
            this.oneStar = "ios-star";
            this.twoStar = "ios-star";
            this.threeStar = "ios-star";
            this.fourStar = "ios-star";
            this.fiveStar = "ios-star";
            this.curRating = 5;
        }
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_8" /* ViewChild */])(__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["n" /* Slides */]),
        __metadata("design:type", __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["n" /* Slides */])
    ], SendfeedPage.prototype, "slides", void 0);
    SendfeedPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-sendfeed',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/sendfeed/sendfeed.html"*/'<ion-header >\n\n		<div class ="profile-blur" [style.background]="\'url(\'+ receivePho +\')\'" ></div>\n\n		<ion-navbar color = "light" transparent>\n		</ion-navbar>\n		<button ion-button small id = "Block-Button" (click) = "blockUser()">\n				<ion-icon name="ios-flag"></ion-icon>\n		</button>\n	\n	<!-- profile pic -->\n	<h2 id = "profile-name"> </h2>\n	<div class = "profile-container">\n\n			<img class="profile-pic" [src] = "receivePho">\n		 <h1 class="profile-name">{{targetFirst}} {{targetLast}}</h1>\n		 <p class = "username"> @{{param.username}}</p>\n 	</div>\n\n</ion-header>\n\n\n\n<ion-content class="has-header">\n	<ion-slides>\n  <ion-slide>\n  	<ion-grid>\n  		<ion-row>\n  			<ion-col>\n  				<ion-label>Anonymous?</ion-label>\n  			</ion-col>\n  			<ion-col>\n  				<ion-toggle [(ngModel)] = "annon" ></ion-toggle>\n  			</ion-col>\n  		</ion-row>\n  		<ion-row>\n  			<ion-col>\n  					<button ion-button (click) = "goToSlide(1,1);" class = "review-or-feedback"> \n					feedback(private)<ion-icon name="ios-lock-outline" style = " display: inline;"></ion-icon>\n					 \n				</button>\n  			</ion-col>\n  			<ion-col>\n  				 <button ion-button *ngIf = "!annon" (click) = "goToSlide(1,0);" class = "review-or-feedback" color = "blue">&nbsp;review(public) &nbsp;\n				 <ion-icon name="md-globe" style = "display: inline;"></ion-icon> \n				</button>\n  			</ion-col>\n  		</ion-row>\n  	</ion-grid>\n   <ion-item no-lines>\n		\n		</ion-item>\n\n<div>\n<h3 >Reviews </h3>\n<ion-list no-lines>\n	<ion-item>\n		<ion-card>\n			<ion-icon [name]="oneLight"></ion-icon> \n			<ion-icon [name]="twoLight"></ion-icon> \n			<ion-icon [name]="threeLight"></ion-icon> \n			<ion-icon [name]="fourLight"></ion-icon> \n			<ion-icon [name]="fiveLight"></ion-icon> \n			<p>Fantastic experience, great pianist, a must see!</p>\n			<div> <ion-icon name = ""></ion-icon></div>\n		</ion-card>\n	</ion-item>\n	<ion-item>\n		<ion-card>\n			Good jobbadandlanflasnflasndfaslndflasnfdla\n		</ion-card>\n	</ion-item>\n		<ion-item>\n		<ion-card>\n			Good jobbadandlanflasnflasndfaslndflasnfdla\n		</ion-card>\n	</ion-item>\n		<ion-item>\n		<ion-card>\n			Good jobbadandlanflasnflasndfaslndflasnfdla\n		</ion-card>\n	</ion-item>\n		<ion-item>\n		<ion-card>\n			Good jobbadandlanflasnflasndfaslndflasnfdla\n		</ion-card>\n	</ion-item>\n</ion-list>\n<!-- <ion-card>\n	<ion-card-content>\n		Kevin is a fantastic pianist. I went to listen to his recital the other day and he played Chopin flawlessly. He indeed is one of the greatest pianist in the 20th century. Definitely recommend goto one of his recitals!He played Chopin\'s 2nd concerto and Ballade No.1 He is fantastic. He is a great guy as well!\n	</ion-card-content>\n</ion-card> -->\n</div>\n  </ion-slide>\n\n  <ion-slide>\n  	<button ion-button class = "go-back-button" (click) = "goBackSlide(0);">	<ion-icon name = "ios-arrow-back"></ion-icon></button>\n	<div class = "text-inputs">\n		<ion-input floating autocorrect  type = "text"[(ngModel)] = "mesData.title" placeholder = "Title, maximum 100 characters" maxlength="100">\n		</ion-input> <button ion-button *ngIf = "mesData.title" class = "go-back-button" (click) = "goToSlide(2);" style = "margin-top:-25rem; margin-left: 14.5rem;"> <ion-icon name = "ios-arrow-forward-outline"> </ion-icon> </button>\n	</div>\n  </ion-slide>\n\n  <ion-slide id = "lastSlide">\n		<textarea type="text" [(ngModel)] = "mesData.message" class = "messageBox" placeholder="Send your candid feedback/review here! Maximum 5000 charaxt" maxlength="5000"></textarea>\n		<button ion-button class = "go-back-button" (click) = "goBackSlide(1);">	<ion-icon name = "ios-arrow-back"></ion-icon></button>\n		<div class = "lightning" *ngIf = "type == \'review\'">\n		<ion-icon [name]="oneStar" (click)  = "clickStar(\'one\')"></ion-icon> \n		<ion-icon [name]="twoStar" (click)  = "clickStar(\'two\')"></ion-icon> \n		<ion-icon [name]="threeStar" (click)  = "clickStar(\'three\')"></ion-icon> \n		<ion-icon [name]="fourStar" (click)  = "clickStar(\'four\')"></ion-icon> \n		<ion-icon [name]="fiveStar" (click)  = "clickStar(\'five\')"></ion-icon> \n		</div>\n		<div style = "text-align: center; margin-top:10px;">\n<!-- 		<button *ngIf = "mesData.message" ion-button color = "primary" id = "submit" (click) = "sendMessage()" >\n		send message\n		</button> -->\n		<button ion-button *ngIf = "mesData.message" (click) = "sendMessage();" class = "sendButton"> <ion-icon name = "md-send"> </ion-icon> </button>\n		\n		</div>\n  </ion-slide>\n\n</ion-slides>\n<!-- Anonymous Toggle -->\n\n<!--  feedback in textbox and title inputs -->\n\n<!-- <div class = "text-inputs">\n		<ion-input floating autocorrect  type = "text"\n						[(ngModel)] = "mesData.title" \n						placeholder = "Title">\n		</ion-input>\n\n		<textarea type="text" [(ngModel)] = "mesData.message"></textarea>\n</div> -->\n\n<!-- sending feedback button -->\n\n\n</ion-content>'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/sendfeed/sendfeed.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["b" /* AlertController */]])
    ], SendfeedPage);
    return SendfeedPage;
}());

//# sourceMappingURL=sendfeed.js.map

/***/ })

});
//# sourceMappingURL=2.js.map
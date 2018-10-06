webpackJsonp([6],{

/***/ 404:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FeedbackPageModule", function() { return FeedbackPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__feedback__ = __webpack_require__(416);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var FeedbackPageModule = /** @class */ (function () {
    function FeedbackPageModule() {
    }
    FeedbackPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__feedback__["a" /* FeedbackPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__feedback__["a" /* FeedbackPage */]),
            ],
        })
    ], FeedbackPageModule);
    return FeedbackPageModule;
}());

//# sourceMappingURL=feedback.module.js.map

/***/ }),

/***/ 416:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return FeedbackPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_chat_info_chat_info__ = __webpack_require__(251);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_5_firebase__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




//simport {FeedbackinfoPage} from '../feedbackinfo/feedbackinfo';



var FeedbackPage = /** @class */ (function () {
    function FeedbackPage(navCtrl, uInfo, chatInfo, afData, alertCtrl) {
        this.navCtrl = navCtrl;
        this.uInfo = uInfo;
        this.chatInfo = chatInfo;
        this.afData = afData;
        this.alertCtrl = alertCtrl;
        this.curList = []; //FOR SWITCHING BETWEEN BETWEEN PUBLIC AND ANNON
        this.feedbackTab = "";
        this.pubArray = [];
        this.annonArray = [];
        this.reloadUser();
        this.reloadFeed();
        //          this.watcherFeed('publicfeedbacks',this.pubArray);
        // this.watcherFeed('anonfeedbacks',this.annonArray);
        // if( !this.usrData ){
        //   setTimeout(() =>{
        //     console.log("waiting for data...");
        //   },2000)
        // }
        // else{
        //   this.watcherFeed('publicfeedbacks',this.pubArray);
        //   this.watcherFeed('anonfeedbacks',this.annonArray);
        // }
        console.log("usrData undefined?", this.usrData);
        // if(this.usrData.feedbacks){
        // }
        // this.setFeedback();
        this.reply = true;
        this.feedbackTab = "Public";
    }
    FeedbackPage.prototype.reloadFeed = function () {
        var _this = this;
        this.usrData = this.uInfo.getUserInfo();
        if (!this.usrData) {
            setTimeout(function () {
                _this.reloadFeed(), 1000;
            });
        }
        else {
            this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child('anonfeedbacks').on('child_added', function (addPub) {
                var value = addPub.val(); //addPub.key
                var key = addPub.key;
                value['key'] = key;
                // var key = this.reloadKey(value,'anonfeedbacks')
                console.log("finally got key!", key);
                console.log("data changed!");
                _this.curListType();
                _this.annonArray.push(value);
            });
            this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child('publicfeedbacks').on('child_added', function (addAnon) {
                var value = addAnon.val();
                var key = addAnon.key; //this.reloadKey(value,'publicfeedbacks')
                value['key'] = key;
                console.log("finally got key!", key);
                console.log("data changed!");
                _this.curListType();
                _this.pubArray.push(value);
            });
        }
    };
    FeedbackPage.prototype.reloadKey = function (value, type) {
        var _this = this;
        this.usrData = this.uInfo.getUserInfo();
        console.log("attempting reload...", this.usrData);
        if (!this.usrData.feedbacks.type[value.id].key) {
            setTimeout(function () {
                _this.reloadKey(value, type), 2000;
            });
        }
        else {
            return this.usrData.feedbacks.anonfeedbacks[value.id].key;
        }
    };
    FeedbackPage.prototype.reloadUser = function () {
        var _this = this;
        this.usrData = this.uInfo.getUserInfo();
        if (this.usrData == undefined) {
            setTimeout(function () {
                _this.usrData = _this.uInfo.getUserInfo(), 2000;
            });
        }
        else {
            if (this.usrData.feedbacks) {
                this.pubMes = this.usrData.feedbacks.publicfeedbacks;
                this.annonMes = this.usrData.feedbacks.anonfeedbacks;
            }
        }
    };
    //---------------REFRESH LIST WHENEVER YOU LOAD THIS PAGE:
    FeedbackPage.prototype.ionViewCanEnter = function () {
        this.setFeedback();
        //   this.setUserInfo();
        //   this.pubMes = this.usrData.publicfeedbacks;
        //   this.annonMes = this.usrData.anonfeedbacks;
    };
    //------------INITIALIZE ARRAYS AND SET DEFAULT PAGE AS PUBLIC-------------------
    FeedbackPage.prototype.setFeedback = function () {
        if (this.usrData.feedbacks) {
            this.pubArray = [];
            this.annonArray = [];
            for (var i in this.pubMes) {
                this.pubArray.push(this.pubMes[i]);
            }
            for (var i in this.annonMes) {
                this.annonArray.push(this.annonMes[i]);
            }
            this.curListType();
        }
        else {
            this.pubArray = [];
            this.annonArray = [];
        }
    };
    //------------WHEN CLICK, GOTO SEARCH USER PAGE-------------
    FeedbackPage.prototype.toSendfeed = function () {
        this.navCtrl.push("SearchuserPage");
    };
    //------Feedback information indepth-------
    /*toLookfeed(mes){
      this.navCtrl.push(FeedbackinfoPage,
        {param: mes,
         reply : this.reply});
    }
    */
    //----------CLICKED PUBLIC----------------------
    FeedbackPage.prototype.clickPub = function () {
        this.feedbackTab = "Public";
        this.curList = this.pubArray;
        console.log("public list clicked!", this.curList);
        this.reply = true;
    };
    //--------------CLICKED ANNON-----------------
    FeedbackPage.prototype.clickAnnon = function () {
        this.feedbackTab = "Anonymous";
        this.curList = this.annonArray;
        console.log("annon list clicked!", this.curList);
        this.reply = false;
    };
    //-----------------------REFRESH MESSAGE-----------------------
    // async setUserInfo(){
    // 		await this.afData.database.ref('users/' + this.usrId).once('value',dataSnap =>{
    // 			this.usrData = dataSnap.val();
    //       this.pubMes = this.usrData.publicfeedbacks;
    //       this.annonMes = this.usrData.anonfeedbacks;
    //       this.setFeedback();
    // 			console.log("reloading data", this.usrData);
    // 		});
    // }
    FeedbackPage.prototype.doRefresh = function (refresher) {
        if (this.usrData.feedbacks) {
            this.usrData = this.uInfo.getUserInfo();
            this.pubMes = this.usrData.feedbacks.publicfeedbacks;
            this.annonMes = this.usrData.feedbacks.anonfeedbacks;
            if (this.feedbackTab == "Public") {
                this.curList = this.pubArray;
                console.log("data changed!", this.curList);
            }
            else {
                this.curList = this.annonArray;
            }
        }
        // this.setUserInfo();
        console.log('Begin async operation', refresher);
        setTimeout(function () {
            console.log('Async operation has ended');
            refresher.complete();
        }, 2000);
    };
    FeedbackPage.prototype.deleteMes = function (mes) {
        var _this = this;
        console.log("message:", mes);
        var alertCtrl = this.alertCtrl.create({
            title: "are you sure you want to delete this feedback?",
            message: "this action is permanent",
            buttons: [
                {
                    text: "no",
                    role: "cancel",
                    handler: function () {
                        console.log("cancel clicked");
                    }
                },
                {
                    text: "yes",
                    handler: function () {
                        _this.delFromList(mes);
                    }
                }
            ]
        });
        alertCtrl.present();
    };
    FeedbackPage.prototype.flagUser = function (mes) {
        var _this = this;
        var alert = this.alertCtrl.create();
        alert.addInput({
            type: "checkbox",
            label: 'Inappropriate Content',
            value: "Inappropriate Content"
        });
        alert.addInput({
            type: "checkbox",
            label: 'Harassment',
            value: "Harassment"
        });
        alert.addInput({
            type: "checkbox",
            label: 'Threats',
            value: "Threats"
        });
        alert.addInput({
            type: "checkbox",
            label: 'Spam',
            value: "Spam "
        });
        alert.addInput({
            type: "text",
            label: 'Other',
            value: "Other"
        });
        alert.addButton('Cancel');
        alert.addButton({
            text: 'Ok',
            handler: function (data) {
                console.log("Radio", data);
                _this.checkboxOpen = false;
                _this.reasons = data;
                var timeStamp = __WEBPACK_IMPORTED_MODULE_5_firebase__["database"].ServerValue.TIMESTAMP;
                _this.afData.database.ref("reports").push({
                    timestamp: timeStamp,
                    reporterid: _this.usrData.id,
                    offenderid: mes.id,
                    reasons: data
                });
                _this.delFromList(mes);
            }
        });
        alert.present().then(function () {
            _this.checkboxOpen = true;
        });
    };
    FeedbackPage.prototype.blockUser = function (mes) {
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
                        blockedUsers[mes.id] = mes.username;
                        blocked[_this.usrData.id] = mes.type;
                        _this.afData.database.ref('users').child(mes.id).child("blocked").update({ blocked: blocked });
                        _this.afData.database.ref('users').child(_this.usrData.id).child('blockedUsers').update(blockedUsers);
                        _this.delFromList(mes);
                    }
                }
            ]
        });
        alert.present();
    };
    FeedbackPage.prototype.delFromList = function (user) {
        var index = null;
        if (user.type == "publicfeedbacks") {
            for (var i in this.pubArray) {
                if (this.pubArray[i].key == user.key) {
                    index = i;
                    break;
                }
            }
            this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child(user.type).child(user.key).remove();
            this.pubArray.splice(index, 1);
            this.curList = this.pubArray;
        }
        else {
            for (var i in this.annonArray) {
                if (this.annonArray[i].key == user.key) {
                    index = i;
                    break;
                }
            }
            this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child(user.type).child(user.key).remove();
            this.annonArray.splice(index, 1);
            this.curList = this.annonArray;
        }
        // if(user.type == "publicfeedbacks"){
        // }
        // else if(user.type = "anonfeedbacks"){
        // }
    };
    //Handle dropdowns
    FeedbackPage.prototype.activateDropdown = function (mes) {
        if (mes.dropdown == true) {
            mes.dropdown = false;
        }
        else {
            mes.dropdown = true;
            for (var i in this.curList) {
                if (this.curList[i].key != mes.key) {
                    this.curList[i].dropdown = false;
                }
            }
        }
    };
    FeedbackPage.prototype.clickMessage = function (mes) {
        var _this = this;
        console.log(mes);
        var alertCtrl = this.alertCtrl.create({
            title: "Report or block the user?",
            buttons: [
                {
                    text: 'Cancel',
                    role: 'cancel',
                    handler: function () {
                        console.log("reviewed message!");
                    }
                },
                {
                    text: "Report",
                    role: "report",
                    handler: function () {
                        _this.flagUser(mes);
                    }
                },
                {
                    text: "Block",
                    role: "block",
                    handler: function () {
                        _this.blockUser(mes);
                    }
                }
            ]
        });
        alertCtrl.present();
    };
    //@param: mes: mes obj, contains info about the feedback
    FeedbackPage.prototype.replyMessage = function (mes) {
        var _this = this;
        console.log(mes);
        var alert = this.alertCtrl.create({
            title: "Message " + mes.username + "?",
            buttons: [
                {
                    text: 'Cancel',
                    role: 'cancel',
                    handler: function () {
                        console.log('Cancel clicked');
                    }
                },
                {
                    text: 'OK',
                    handler: function () {
                        console.log('OK clicked');
                        _this.enterChat(mes);
                    }
                }
            ]
        });
        alert.present();
    };
    FeedbackPage.prototype.curListType = function () {
        if (this.feedbackTab == "Public") {
            this.curList = this.pubArray;
        }
        else {
            this.curList = this.annonArray;
        }
    };
    // watcherFeed(type,type2){
    //      this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child(type).on('child_added', addFeed => {
    //        if(!addFeed.val().key){
    //          // setTimeout(() => {
    //          //   this.,1500;
    //          // })
    //        }
    //        else{
    //           this.afData.database.ref('users').child(this.usrData.id).child('feedbacks').child(type).child('key').on('child_added', furtherFeed => {
    //           var obj = addFeed.val();
    //           obj['key'] = furtherFeed.val();
    //           type2.push(addFeed.val());
    //           console.log("updated array?",type);
    //           this.curListType();
    //       });
    //        }
    //         });
    // }
    //NavParams: chatID which is the ID of the chat itself, and otherID which is the ID of the other person
    FeedbackPage.prototype.enterChat = function (feedback) {
        var _this = this;
        var chatKey = this.chatInfo.checkChat(this.usrId, feedback.id);
        chatKey.then(function (key) {
            if (key) {
                console.log("Chat is found", key);
                _this.navCtrl.push('MessageDetailPage', { chatID: key, otherID: feedback.id });
            }
            else {
                var createNewChat = _this.chatInfo.createNewChat(_this.usrId, feedback.id);
                createNewChat.then(function (newChatKey) {
                    _this.navCtrl.push('MessageDetailPage', { chatID: newChatKey, otherID: feedback.id });
                });
            }
        });
    };
    FeedbackPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-feedback',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/feedback/feedback.html"*/'<ion-header no-border>\n  <ion-navbar color = "transparent">\n   \n   <ion-buttons >\n      <h1 color = primary id = "Listen-Up">ListenUp</h1><button  ion-button icon-only menuToggle class = "menu-button" side="left" class = "menu-button" >  \n\n        <ion-icon name = "ios-menu"></ion-icon>\n      </button>\n    </ion-buttons>\n  </ion-navbar>\n\n  <ion-toolbar color = "primary" style="min-height: 3rem;">\n  	<ion-segment [(ngModel)]="feedbackTab" color = "light" >\n  		<ion-segment-button value="Public" (click) = "clickPub()" class = "segment-button-left">Public</ion-segment-button>\n  		<ion-segment-button value="Anonymous" Anonymous (click) = "clickAnnon()"  class = "segment-button-right"> Anonymous </ion-segment-button>\n  	</ion-segment>\n  </ion-toolbar>\n\n</ion-header>\n\n  \n<ion-content padding >\n  <ion-fab right bottom (click) = "clickPub()" >\n    <button ion-fab color="light" (click) = "toSendfeed()" >\n      <!-- <ion-icon color="primary" name = "noted-logo" ></ion-icon> -->\n      <img src="assets/imgs/fab.png">\n    </button>\n  </ion-fab>\n\n<!--     </button> -->\n  <ion-refresher pulling-text="Pull to refresh..." (ionRefresh) = "doRefresh($event)">\n     <ion-refresher-content\n      pullingIcon="arrow-dropdown"\n      pullingText="Pull to refresh"\n      refreshingSpinner="circles">\n    </ion-refresher-content>\n  </ion-refresher>\n\n  <div class = "feedback-cards">\n      <ion-list >\n          <ng-container *ngFor = "let mes of curList">\n              <ion-item-sliding >\n                    <ion-item >\n                          <ng-container  >\n                                <ion-avatar><img [src] = \'mes.photourl\' (click) = "activateDropdown(mes)">\n                                 </ion-avatar>\n                                  <p  (click) = "activateDropdown(mes)"  class = "first-name"> {{mes.firstname}} </p>\n                                 <div class = "title-pic-container">\n                                     <h2 (click) = "activateDropdown(mes)" color = "primary"  class = "title-and-name">{{mes.title}}</h2>\n                                     <p id = "user-name">@{{mes.username}}</p>\n                                 </div>\n                          </ng-container>\n<!--                           <ion-icon item-end name="ios-arrow-down-outline" color="light" (click) = "activateDropdown(mes)">\n                          </ion-icon> -->\n                    </ion-item>\n                     <ion-item-options >\n                          <button ion-button (click)= "deleteMes(mes)">Delete</button>\n                    </ion-item-options>\n              </ion-item-sliding>\n              <!-- Dropdown -->\n              <ion-card *ngIf="mes.dropdown">\n                  <ion-card-content class = "message-content">\n                    {{mes.message}}\n                  </ion-card-content>\n                  <ion-row>\n                      <ion-col>\n                          <button ion-button icon-left clear small color="danger" (click)="clickMessage(mes)">\n                              <ion-icon name="ios-flag"></ion-icon> Report\n                          </button>\n                      </ion-col>\n                      <ion-col>\n                          <button ion-button icon-right float-right clear small color="primary" (click)="enterChat(mes)">\n                          Message <ion-icon name="ios-chatbubbles" ></ion-icon>\n                          </button>\n                      </ion-col>\n                  </ion-row>\n              </ion-card>\n          </ng-container>\n        </ion-list>\n    </div>\n  </ion-content>'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/feedback/feedback.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_3__providers_chat_info_chat_info__["a" /* ChatInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["b" /* AlertController */]])
    ], FeedbackPage);
    return FeedbackPage;
}());

//# sourceMappingURL=feedback.js.map

/***/ })

});
//# sourceMappingURL=6.js.map
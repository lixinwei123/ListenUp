webpackJsonp([5],{

/***/ 398:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MessageDetailPageModule", function() { return MessageDetailPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__message_detail__ = __webpack_require__(407);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



// import { IonicImageLoader } from 'ionic-image-loader';
var MessageDetailPageModule = /** @class */ (function () {
    function MessageDetailPageModule() {
    }
    MessageDetailPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__message_detail__["a" /* MessageDetailPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__message_detail__["a" /* MessageDetailPage */]),
            ],
        })
    ], MessageDetailPageModule);
    return MessageDetailPageModule;
}());

//# sourceMappingURL=message-detail.module.js.map

/***/ }),

/***/ 407:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return MessageDetailPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_chat_info_chat_info__ = __webpack_require__(251);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__ = __webpack_require__(23);
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


// Providers


//import { UserInfo } from '@firebase/auth-types';




/**
 * Generated class for the MessageDetailPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var MessageDetailPage = /** @class */ (function () {
    function MessageDetailPage(navCtrl, chatInfo, uInfo, navParams, alertCtrl, afData, sheetCtrl) {
        this.navCtrl = navCtrl;
        this.chatInfo = chatInfo;
        this.uInfo = uInfo;
        this.navParams = navParams;
        this.alertCtrl = alertCtrl;
        this.afData = afData;
        this.sheetCtrl = sheetCtrl;
        //Initialize variables
        this.chatID = this.navParams.get('chatID');
        console.log("chat key", this.chatID);
        this.otherID = this.navParams.get('otherID');
        console.log("what is other id", this.otherID);
        this.usrID = this.uInfo.getUserInfo().id;
        //Call functions here
        this.getOtherInfo();
        this.loadMessages();
        this.loadOtherInfo();
    }
    MessageDetailPage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad MessageDetailPage');
    };
    MessageDetailPage.prototype.getOtherInfo = function () {
        var _this = this;
        this.afData.database.ref('users').child(this.otherID).once('value', function (dataSnap) {
            _this.otherInfo = dataSnap.val();
            // if(!this.otherInfo){
            //   setTimeout(() =>{
            //     this.otherInfo = dataSnap.val
            //   })
            // }
            console.log("other info", _this.otherInfo);
        });
    };
    MessageDetailPage.prototype.loadMessages = function () {
        this.chatData = this.chatInfo.loadMessages(this.chatID);
    };
    MessageDetailPage.prototype.loadOtherInfo = function () {
        var _this = this;
        this.uInfo.getOtherUserInfo(this.otherID).subscribe(function (otherPersonData) {
            _this.otherData = otherPersonData;
            console.log(_this.otherData);
        });
    };
    MessageDetailPage.prototype.sendMessage = function (text) {
        this.chatInfo.addMessage(text, this.usrID, this.otherID, this.chatID);
        this.messageText = "";
    };
    MessageDetailPage.prototype.logChat = function (chat) {
        console.log(chat.sender);
        // console.log(this.usrId)
    };
    MessageDetailPage.prototype.reportUser = function () {
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
                    reporterid: _this.usrID,
                    offenderid: _this.otherID,
                    reasons: data
                });
                _this.navCtrl.pop();
            }
        });
        alert.present().then(function () {
            _this.checkboxOpen = true;
        });
    };
    MessageDetailPage.prototype.blockUser = function () {
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
                        var blockedusers = {};
                        blockedusers[_this.otherID] = _this.otherInfo.username;
                        _this.afData.database.ref('users').child(_this.usrID).update({ blockedusers: blockedusers });
                        _this.navCtrl.pop();
                    }
                }
            ]
        });
        alert.present();
    };
    MessageDetailPage.prototype.flagUser = function () {
        var _this = this;
        var actionSheet = this.sheetCtrl.create({
            title: 'Report or block this user?',
            buttons: [
                {
                    text: 'Report',
                    role: 'report',
                    handler: function () {
                        _this.reportUser();
                    }
                },
                {
                    text: 'Block',
                    role: 'block',
                    handler: function () {
                        _this.blockUser();
                    }
                },
                {
                    text: 'Cancel',
                    role: 'cancel',
                    handler: function () {
                        console.log("canceled clicked");
                    }
                }
            ]
        });
        actionSheet.present();
    };
    MessageDetailPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-message-detail',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/message-detail/message-detail.html"*/'<!--\n  Generated template for the MessageDetailPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n  <ion-navbar color="primary">\n    <!-- <ion-item no-lines color="primary">\n         <ion-avatar item-left><img [src]="otherData?.photourl"></ion-avatar>\n        <p>{{otherData?.firstname}} {{otherData?.lastname}}</p>\n    </ion-item>  -->\n    <ion-title> <span class = "name-title">{{otherData?.firstname}} {{otherData?.lastname}}</span></ion-title>\n  </ion-navbar>\n  <button ion-button small id = "flag-Button" (click) = "flagUser()">\n    <ion-icon name="ios-flag"></ion-icon>\n  </button>\n\n</ion-header>\n\n\n<ion-content padding>\n  <ion-list no-lines>\n    <ion-item *ngFor="let chat of chatData | async" (click)="logChat(chat)">\n      <!-- If you\'re the sender -->\n      <ion-card text-wrap class="message-sender">\n        <ion-card-content *ngIf="chat.sender == usrID">{{chat.text}}</ion-card-content>\n\n      </ion-card>\n\n      <!-- If you\'re the receiver -->\n      <ion-card text-wrap class = "message-receiver" *ngIf="chat.receiver == usrID">\n          <ion-card-content>{{chat.text}}</ion-card-content>\n      </ion-card>\n\n\n    </ion-item>\n  </ion-list>\n\n</ion-content>\n\n\n<ion-footer>\n    <ion-toolbar>\n      <form>\n        <ion-item>\n          <ion-input autocomplete autocorrect type="text" placeholder="Write a message" name="messageText" [(ngModel)]="messageText"></ion-input>\n        </ion-item>\n      </form>\n\n      <ion-buttons end>\n        <button ion-button icon-right color="primary" (click)="sendMessage(messageText)">\n          Send\n          <ion-icon name="send"></ion-icon>\n        </button>\n      </ion-buttons>\n    </ion-toolbar>\n  </ion-footer>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/message-detail/message-detail.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_2__providers_chat_info_chat_info__["a" /* ChatInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["b" /* AlertController */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["a" /* ActionSheetController */]])
    ], MessageDetailPage);
    return MessageDetailPage;
}());

//# sourceMappingURL=message-detail.js.map

/***/ })

});
//# sourceMappingURL=5.js.map
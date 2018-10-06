webpackJsonp([4],{

/***/ 400:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ProfilePageModule", function() { return ProfilePageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__profile__ = __webpack_require__(413);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



//import { BarcodeScanner } from '@ionic-native/barcode-scanner';
// import { IonicImageLoader } from 'ionic-image-loader';
var ProfilePageModule = /** @class */ (function () {
    function ProfilePageModule() {
    }
    ProfilePageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__profile__["a" /* ProfilePage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__profile__["a" /* ProfilePage */]),
            ],
            exports: [
                __WEBPACK_IMPORTED_MODULE_2__profile__["a" /* ProfilePage */]
            ],
            entryComponents: [
                __WEBPACK_IMPORTED_MODULE_2__profile__["a" /* ProfilePage */]
            ]
        })
    ], ProfilePageModule);
    return ProfilePageModule;
}());

//# sourceMappingURL=profile.module.js.map

/***/ }),

/***/ 413:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ProfilePage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__ionic_native_camera__ = __webpack_require__(252);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_5_firebase__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__pages_login_login__ = __webpack_require__(65);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__ionic_native_barcode_scanner__ = __webpack_require__(253);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};











var ProfilePage = /** @class */ (function () {
    function ProfilePage(navCtrl, uInfo, Camera, navParams, afData, actSheet, afAuth, app, alertCtrl, scanner) {
        this.navCtrl = navCtrl;
        this.uInfo = uInfo;
        this.Camera = Camera;
        this.navParams = navParams;
        this.afData = afData;
        this.actSheet = actSheet;
        this.afAuth = afAuth;
        this.app = app;
        this.alertCtrl = alertCtrl;
        this.scanner = scanner;
        this.encodText = '';
        this.encodedData = {};
        this.scannedData = {};
        this.loadUserInfo();
        this.background = this.uInfo.getDefault();
        if (this.background) {
            this.receivePho = this.uInfo.getPhoto();
        }
    }
    ProfilePage.prototype.scan = function () {
        var _this = this;
        this.options = {
            prompt: 'Scan your Barcode'
        };
        this.scanner.scan(this.options).then(function (data) {
            _this.scannedData = data;
        }, function (err) {
            console.log('Error :', err);
        });
    };
    ProfilePage.prototype.encode = function () {
        var _this = this;
        this.scanner.encode(this.scanner.Encode.TEXT_TYPE, this.usrInfo.id).then(function (data) {
            _this.encodedData = data;
        }, function (err) {
            console.log('Error :', err);
        });
    };
    ProfilePage.prototype.loadUserInfo = function () {
        var _this = this;
        this.usrInfo = this.uInfo.getUserInfo();
        if (!this.usrInfo) {
            setTimeout(function () {
                _this.loadUserInfo();
            }, 1000);
        }
        else {
            this.firstName = this.usrInfo.firstname;
            this.lastName = this.usrInfo.lastname;
            this.userName = this.usrInfo.username;
            this.userPhoto = this.uInfo.getPhoto();
        }
    };
    ProfilePage.prototype.capture = function (sourcetype) {
        var _this = this;
        var cameraOptions = {
            quality: 50,
            destinationType: this.Camera.DestinationType.DATA_URL,
            encodingType: this.Camera.EncodingType.JPEG,
            mediaType: this.Camera.MediaType.PICTURE,
            sourceType: sourcetype
        };
        this.Camera.getPicture(cameraOptions).then(function (imageData) {
            _this.captureDataUrl = 'data:image/jpeg;base64,' + imageData;
            _this.receivePho = _this.captureDataUrl;
            _this.upload();
        }, function (err) {
        });
    };
    ProfilePage.prototype.upload = function () {
        var storageRef = __WEBPACK_IMPORTED_MODULE_5_firebase__["storage"]().ref(); //reference to storage database
        var imageRef = storageRef.child("profiles/" + this.uInfo.getUserId() + ".jpg");
        imageRef.putString(this.captureDataUrl, __WEBPACK_IMPORTED_MODULE_5_firebase__["storage"].StringFormat.DATA_URL).then(function (snapshot) {
        });
        this.afData.database.ref("users").child(this.usrInfo.id).update({
            photourl: this.captureDataUrl
        });
    };
    ProfilePage.prototype.setPhoto = function () {
        var _this = this;
        var actSheet = this.actSheet.create({
            title: 'Choose a Photo Option',
            buttons: [
                {
                    text: 'Gallery',
                    role: 'upload',
                    handler: function () {
                        console.log("uploading photo clicked");
                        _this.capture(0);
                    }
                },
                {
                    text: 'Camera',
                    role: 'take',
                    handler: function () {
                        console.log("clicked take photo");
                        _this.capture(1);
                    }
                },
                {
                    text: 'Cancel',
                    role: 'cancel',
                    handler: function () {
                        console.log("cancel clicked");
                    }
                }
            ]
        });
        actSheet.present();
    };
    ProfilePage.prototype.toFeedback = function () {
        this.navCtrl.push("SearchuserPage");
    };
    ProfilePage.prototype.logoutClicked = function () {
        var _this = this;
        var alertCtrl = this.alertCtrl.create({
            title: 'Are you sure you want to log out?',
            buttons: [{
                    text: "Logout",
                    role: "Logout",
                    handler: function () {
                        console.log('Logout...');
                        _this.afAuth.auth.signOut();
                        _this.uInfo.clearUserInfo();
                        var nav = _this.app.getRootNav();
                        nav.setRoot(__WEBPACK_IMPORTED_MODULE_6__pages_login_login__["a" /* LoginPage */]);
                    }
                },
                {
                    text: "Cancel",
                    role: "cancel"
                }
            ]
        });
        alertCtrl.present();
    };
    ProfilePage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-profile',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/profile/profile.html"*/'<ion-header>\n  <div class = "profile-blur" [style.background]="\'url(\'+ receivePho +\')\'"></div>\n  \n  <ion-navbar transparent>\n\n   <h1>ListenUp</h1>\n    <ion-buttons >\n<!-- <<<<<<< HEAD\n       <button ion-button icon-only menuToggle class = "menu-button" side="left" class = "menu-button" >\n        <ion-icon name = "ios-menu"></ion-icon>\n======= -->\n       <button ion-button icon-only menuToggle class = "menu-button">\n        <ion-icon name = "ios-menu-outline"></ion-icon>\n      </button>\n      <!-- <button ion-button (click) =  "logoutClicked();" ion-button class = "log-out". >\n          <ion-icon name = "ios-menu-outline"></ion-icon>\n        </button> -->\n <!--      <button ion-button icon-only menuToggle class = "menu-button" side="left"> -->\n   <!--      Listen Up\n>>>>>>> bd879bc56a45e414e970cbbbd2657ca166c5e42b -->\n<!--       </button> -->\n    </ion-buttons>\n  </ion-navbar>\n\n  <img class="profile-photo" [src] = "captureDataUrl ? captureDataUrl : userPhoto" (click) = "setPhoto()">\n  <h1> {{firstName}} {{lastName}}</h1>\n  <h2 id="A1">@{{userName}}</h2>\n</ion-header>\n\n<ion-content padding>\n\n  \n  \n  \n <!-- <img class = "ur-code" src="assets/imgs/qrcode.png" (click)="toFeedback()">-->\n<!--  <div>\n <ion-input style="background-color:#808080" type = "text" [(ngModel)]="encodText"> </ion-input>\n <button ion-button block (click)="encode()" >Encode</button>\n</div>\n <div>\n <button ion-button block (click)="scan()" >Scan</button>\n <div *ngIf="scannedData.txt">\n <label>Your barcode is</label>\n <br>\n <span>{{scannedData.text}}</span>\n</div>\n</div> -->\n\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/profile/profile.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_2__ionic_native_camera__["a" /* Camera */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["a" /* ActionSheetController */],
            __WEBPACK_IMPORTED_MODULE_7_angularfire2_auth__["a" /* AngularFireAuth */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["c" /* App */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["b" /* AlertController */], __WEBPACK_IMPORTED_MODULE_8__ionic_native_barcode_scanner__["a" /* BarcodeScanner */]])
    ], ProfilePage);
    return ProfilePage;
}());

//# sourceMappingURL=profile.js.map

/***/ })

});
//# sourceMappingURL=4.js.map
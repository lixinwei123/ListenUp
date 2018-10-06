webpackJsonp([12],{

/***/ 123:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BlockusersPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__ = __webpack_require__(23);
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
 * Generated class for the BlockusersPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var BlockusersPage = /** @class */ (function () {
    // blockedObj: any;
    function BlockusersPage(navCtrl, navParams, afData, alertCtrl, uInfo) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.afData = afData;
        this.alertCtrl = alertCtrl;
        this.uInfo = uInfo;
        this.usrData = this.uInfo.getUserInfo();
        this.blockedArray = this.usrData.blockedUsers;
        this.filterArray = [];
        for (var i in this.usrData.blockedUsers) {
            if (this.usrData.blockedUsers[i] != "annonymous") {
                var obj = {};
                obj[i] = this.usrData.blockedUsers[i];
                this.filterArray.push(this.usrData.blockedUsers[i]);
            }
        }
    }
    BlockusersPage.prototype.ionViewDidLoad = function () {
    };
    BlockusersPage.prototype.searchUsers = function (searchbar) {
        var q = searchbar.srcElement.value;
        console.log("searching...", q);
        if (!q)
            return;
        if (String(q).replace(/\s/g, "").length == 0) {
            return true;
        }
        this.filterArray = this.filterArray.filter(function (v) {
            if (v && q) {
                if (v.toLowerCase().indexOf(q.toLowerCase()) > -1) {
                    return true;
                }
                return false;
            }
        });
    };
    BlockusersPage.prototype.unblock = function (user) {
        var _this = this;
        console.log("user", user);
        var uid = "";
        for (var i in this.blockedArray) {
            if (this.blockedArray[i] == user) {
                console.log("i is", i);
                uid = i;
                break;
            }
        }
        var alertCtrl = this.alertCtrl.create({
            title: 'unblock this user?',
            message: 'he can search you and send feedback to you again',
            buttons: [
                {
                    text: 'no',
                    role: 'cancel',
                    handler: function () {
                        console.log("pressed no");
                    }
                },
                {
                    text: 'yes',
                    handler: function () {
                        console.log("unblocked user");
                        _this.afData.database.ref('users').child(uid).child("blocked").child(_this.usrData.id).remove();
                        _this.afData.database.ref('users').child(_this.usrData.id).child("blockedUsers").child(uid).remove();
                        // this.blocked = false;
                        var index = _this.filterArray.indexOf(user);
                        _this.filterArray.splice(index, 1);
                    }
                }
            ]
        });
        alertCtrl.present();
    };
    BlockusersPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-blockusers',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/blockusers/blockusers.html"*/'<!--\n  Generated template for the BlockusersPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n  <ion-navbar color = "primary">\n    <ion-title><ion-searchbar autocomplete autocorrect placeholder = "Enter username to search" (ionInput) = "searchUsers($event)"></ion-searchbar></ion-title>\n<!--     <ion-toolbar >\n    	  \n    </ion-toolbar> -->\n  </ion-navbar>\n</ion-header>\n\n\n<ion-content padding>\n<ion-list>\n	<ion-item *ngFor = "let user of filterArray">\n		@{{user}} <button ion-button (click) = "unblock(user)">Unblock</button>\n	</ion-item>\n</ion-list>\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/blockusers/blockusers.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["b" /* AlertController */],
            __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__["a" /* UserInfoProvider */]])
    ], BlockusersPage);
    return BlockusersPage;
}());

//# sourceMappingURL=blockusers.js.map

/***/ }),

/***/ 124:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return RegisterPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__createuser_createuser__ = __webpack_require__(66);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__termsofservice_modal__ = __webpack_require__(205);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};








var RegisterPage = /** @class */ (function () {
    //CONSTRUCTOR: all the things that have to be loaded to run the page
    function RegisterPage(afAuth, navCtrl, navParams, afData, uInfo, mdCtrl) {
        this.afAuth = afAuth;
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.afData = afData;
        this.uInfo = uInfo;
        this.mdCtrl = mdCtrl;
        // regPass: RegExp = /(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}/;
        //VARIABLES TO BE USED
        this.user = {
            email: "",
            password: "",
            repass: "",
            cEmail: ""
        };
    }
    RegisterPage.prototype.registerPeople = function () {
        var _this = this;
        if (this.user.password == this.user.repass && this.user.cEmail == this.user.email /*&& this.regPass.test(this.user.password)*/) {
            this.afAuth.auth.createUserWithEmailAndPassword(this.user.email, this.user.password)
                .then(function (success) {
                _this.infoVar = {
                    id: success.uid,
                    email: _this.user.email,
                };
                _this.afData.database.ref('users').child(_this.infoVar.id).update(_this.infoVar);
                _this.navCtrl.setRoot(__WEBPACK_IMPORTED_MODULE_5__createuser_createuser__["a" /* CreateuserPage */]);
            })
                .catch(function (err) {
                console.log(err.message);
            });
        }
        else {
            console.log("something happend! fix itttttt");
            return;
        }
    };
    RegisterPage.prototype.showTermofServiceModal = function () {
        var modal = this.mdCtrl.create(__WEBPACK_IMPORTED_MODULE_6__termsofservice_modal__["a" /* TermsOfServiceModal */]);
        //
        // modal.onDidDismiss(data => {
        //   //console.log("User ", data);
        // });
        modal.present();
    };
    RegisterPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-register',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/register/register.html"*/'<!--\n  Generated template for the RegisterPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n  <ion-navbar>\n    <ion-title>Registration</ion-title>\n  </ion-navbar>\n\n</ion-header>\n\n\n<ion-content padding>\n\n  <ion-item>\n  <ion-label floating>Email Address</ion-label>\n  <ion-input type="text" [(ngModel)]="user.email"></ion-input>\n  </ion-item>\n\n   <ion-item>\n  <ion-label floating>Confirm Email Address</ion-label>\n  <ion-input type="text" [(ngModel)]="user.cEmail"></ion-input>\n  </ion-item>\n\n  <ion-item>\n  <ion-label floating>Password</ion-label>\n  <ion-input type="password" [(ngModel)]="user.password"></ion-input>\n  </ion-item>\n\n   <ion-item>\n  <ion-label floating>Re-enter Password</ion-label>\n  <ion-input type="password" [(ngModel)]="user.repass"></ion-input>\n  </ion-item>\n\n <div class ="Terms-of-Agreement">\n    <ion-item>\n      <ion-label >By signing up, you agree to our \n        <button ion-button clear (click) = "showTermofServiceModal()"> <u><b>Term of Services</b></u></button>\n    </ion-label>\n  </ion-item>\n  </div>\n  \n  <button ion-button (click)="registerPeople()" color = "#76a5af">Continue</button>\n\n\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/register/register.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_2_angularfire2_auth__["a" /* AngularFireAuth */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_3_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_4__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["j" /* ModalController */]])
    ], RegisterPage);
    return RegisterPage;
}());

//# sourceMappingURL=register.js.map

/***/ }),

/***/ 135:
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncatched exception popping up in devtools
	return Promise.resolve().then(function() {
		throw new Error("Cannot find module '" + req + "'.");
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = 135;

/***/ }),

/***/ 177:
/***/ (function(module, exports, __webpack_require__) {

var map = {
	"../pages/blockusers/blockusers.module": [
		395,
		11
	],
	"../pages/createuser/createuser.module": [
		396,
		10
	],
	"../pages/feedback/feedback.module": [
		404,
		6
	],
	"../pages/feedbacktitle/feedbacktitle.module": [
		397,
		9
	],
	"../pages/login/login.module": [
		405,
		8
	],
	"../pages/message-detail/message-detail.module": [
		398,
		5
	],
	"../pages/message/message.module": [
		399,
		0
	],
	"../pages/profile/profile.module": [
		400,
		4
	],
	"../pages/register/register.module": [
		401,
		7
	],
	"../pages/searchuser/searchuser.module": [
		402,
		3
	],
	"../pages/sendfeed/sendfeed.module": [
		406,
		2
	],
	"../pages/settings/settings.module": [
		403,
		1
	]
};
function webpackAsyncContext(req) {
	var ids = map[req];
	if(!ids)
		return Promise.reject(new Error("Cannot find module '" + req + "'."));
	return __webpack_require__.e(ids[1]).then(function() {
		return __webpack_require__(ids[0]);
	});
};
webpackAsyncContext.keys = function webpackAsyncContextKeys() {
	return Object.keys(map);
};
webpackAsyncContext.id = 177;
module.exports = webpackAsyncContext;

/***/ }),

/***/ 205:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TermsOfServiceModal; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var TermsOfServiceModal = /** @class */ (function () {
    function TermsOfServiceModal(viewCtrl) {
        this.viewCtrl = viewCtrl;
    }
    TermsOfServiceModal.prototype.dismiss = function (isCreated) {
        this.viewCtrl.dismiss(isCreated);
    };
    TermsOfServiceModal = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/register/termsofservice-modal.html"*/'<ion-header>\n  <ion-toolbar color="primary">\n\n    <!-- cancel buttton -->\n    <!-- <ion-buttons start>\n      <button ion-button color="light" (click)="disagree()">Disagree</button>\n    </ion-buttons> -->\n\n    <ion-title>Terms of Service</ion-title>\n\n    <!-- close button -->\n    <ion-buttons end>\n      <button ion-button icon-only color="light" (click)="dismiss()">\n        <ion-icon name="ios-arrow-down"></ion-icon>\n      </button>\n    </ion-buttons>\n\n  </ion-toolbar>\n</ion-header>\n\n\n\n\n<ion-content padding>\n\n  <h5 class="TOSCategory">Privacy</h5>\n        <p>\n          Your privacy is very important to us. We designed our Privacy Policy to make\n          important disclosures about how you can use ListenUp, a product of Dreality LLC., to\n          share with others and how we collect and can use your content and information. We\n          encourage you to read the Privacy Policy and to use it to help you make informed\n          decisions.\n        </p>\n        <h5 class="TOSCategory">Sharing Your Content and Information </h5>\n        <p>You own all of the content and information you post on ListenUp, and you can control\n          how it is shared through your privacy and application settings. In addition:\n        </p>\n\n        <p>For content that is covered by intellectual property rights, like photos (IP\ncontent), you specifically give us the following permission,\nsubject to your privacy and application settings: you grant\nus a non-exclusive, transferable, sub-licensable, royalty free,\nworldwide license to use any IP content that you post\non or in connection with ListenUp (IP License). This IP License\nends when you delete your IP content or your account\nunless your content has been shared with others, and they\nhave not deleted it.</p>\n<p>• When you delete IP content, it is deleted in a manner similar to emptying\nthe recycle bin on a computer. However, you understand that removed content may\npersist in backup copies for a reasonable period of time (but will not be available to\nothers).<p>\n<p>• By submitting, posting or displaying Content on or through the Services,\nyou grant us a worldwide, non-exclusive, royalty-free license (with\nthe right to sublicense) to use, copy, reproduce, process, adapt,\nmodify, publish, transmit, display and distribute such Content.\nSafety</p>\n<p>We do our best to keep ListenUp safe, but we cannot guarantee it. ListenUp is not\nresponsible for the conduct of any user on or off of the Services. We need your\nhelp to keep ListenUp safe, which includes the following commitments by you:</p>\n<p>• You will not post unauthorized commercial communications (such as\nspam) on ListenUp.</p>\n<p>• You will not collect users\' content or information, or otherwise access\nListenUp, using automated means (such as harvesting bots,\nrobots, spiders, or scrapers) without our prior permission.</p>\n<p>• You will not engage in unlawful multi-level marketing, such as a pyramid\nscheme, on ListenUp.</p>\n<p>• You will not upload viruses or other malicious code.</p>\n<p>• You will not solicit login information or access an account belonging to\nsomeone else.</p>\n<p>• You will not bully, intimidate, or harass any user.</p>\n<p>• You will not post content that: is hate speech, threatening, or\ngraphic or gratuitous violence.</p>\npornographic; incites violence; or contains nudity or\n<p>• You will not develop or operate a third-party application containing\nalcohol-related, dating or other mature content (including\nadvertisements) without appropriate age-based\nrestrictions.</p>\n<p>• You will not use ListenUp to do anything unlawful, misleading, malicious, or\ndiscriminatory.</p>\n<p>• You will not do anything that could disable, overburden, or impair the\nproper working or appearance of ListenUp, such as a denial of\nservice attack or interference with page rendering or other\nListenUp functionality.</p>\n<p>• You will not facilitate or encourage any violations of this Statement or our\npolicies.</p>\nRegistration and Account Security\n<p>• You will not provide any false personal information on ListenUp, or create an\naccount for anyone other than yourself without permission.</p>\n<p>• You will not create more than one personal account.</p>\n<p>• If we disable your account, you will not create another one without our\npermission.</p>\n<p>• You will not use your personal timeline primarily for your own commercial\ngain, and will use a ListenUp Page for such purposes.</p>\n<p>• You will not use ListenUp if you are under 18.</p>\n<p>• You will not use ListenUp if you are a convicted sex offender.</p>\n<p>• You will keep your contact information accurate and up-to-date.</p>\n<p>• You will not share your password (or in the case of developers, your secret\nkey), let anyone else access your account, or do anything else\nthat might jeopardize the security of your account.<p>\n    <h5 class="TOSCategory">Community Rules: Protecting Other People\'s Rights </h5>\n\n<p>• You will not post content or take any action on ListenUp that infringes or\nviolates someone else\'s rights or otherwise violates the law. </p>\n<p>• We can remove any content or information you post on ListenUp if we believe\nthat it violates this Statement or our policies. </p>\n<p>• You agree to use caution in all interactions with other users, particularly if\nyou decide to communicate off the Service or meet in person. </p>\n<p>• You will not post anyone\'s identification documents or sensitive financial\ninformation on ListenUp. </p>\n<p>• You will not add users or send email invitations to non-users without their\nconsent. </p>\n<p>• You will not use the Service for any purpose that is illegal or prohibited by\nthis Agreement. </p>\n<p>• You will not spam, solicit money from or defraud any users. </p>\n<p>• You will not impersonate any person or entity or post any images of another\nperson without his or her permission. </p>\n<p>• You will not bully, “stalk,” intimidate, harass or defame any person. </p>\n<p>• You will not post any Content that is hate speech, threatening, sexually\nexplicit or pornographic; incites violence; or contains nudity or\ngraphic or gratuitous violence. </p>\n<p>• You will not post any Content that promotes racism, bigotry, hatred or\nphysical harm of any kind against any group or individual. </p>\n<p>• You will not solicit passwords for any purpose, or personal identifying\ninformation for commercial or unlawful purposes from other\nusers or disseminate another person’s personal information\nwithout his or her permission. </p>\n<p>• You will not use another user’s account.<p>\n<p>ListenUp reserves the right to investigate and/ or terminate your account without a refund\nof any purchases if you have misused the Service or behaved in a way that ListenUp\nregards as inappropriate or unlawful, including actions or communications that occur off\nthe Service but involve users you meet through the Service.</p>\n<p>Please also remember that despite our offering of anonymity your activity may have\nconsequences that could lead to criminal and civil liability.\nMobile and Other Devices </p>\n<p>• We currently provide our mobile services for free, but please be\naware that your carrier\'s normal rates and fees, such as\ntext messaging and data charges, will still apply. </p>\n<p>• In the event you change or deactivate your mobile telephone\nnumber, you will update your account information on ListenUp\nwithin 48 hours to ensure that your messages are not sent\nto the person who acquires your old number. </p>\n<p>• You provide consent and all rights necessary to enable users to\nsync (including through an application) their devices with\nany information that is visible to them on ListenUp.\nSpecial Provisions Applicable to Software </p>\n<p>• If you download or use our software, such as a stand-alone\nsoftware product, an app, or a browser plugin, you agree\nthat from time to time, the software may download and\ninstall upgrades, updates and additional features from us\nin order to improve, enhance, and further develop the\nsoftware. </p>\n<p>• You will not modify, create derivative works of, decompile, or\notherwise attempt to extract source code from us, unless\nyou are expressly permitted to do so under an open source\nlicense, or we give you express written permission.\nAmendments </p>\n<p>• We’ll notify you before we make changes to these terms and give\nyou the opportunity to review and comment on the revised\nterms before continuing to use our Services. </p>\n<p>• If we make changes to policies, guidelines or other terms\nreferenced in or incorporated by this Statement, we may\nprovide notice via email. </p>\n<p>• Your continued use of the ListenUp Services, following notice of the\nchanges to our terms, policies or guidelines, constitutes\nyour acceptance of our amended terms, policies or\nguidelines.</p>\n\n\n        <h5 class="TOSCategory">Termination </h5>\n\n\n        <p>If you violate the letter or spirit of this Statement, or otherwise create risk or\npossible legal exposure for us, we can stop providing all or part of ListenUp to you.\nWe will notify you by email or at the next time you attempt to access your\naccount. You may also delete your account or disable your application at any\ntime. </p>\n\n\n        <h5 class="TOSCategory">Feedback </h5>\n\n\n        <p>The more suggestions our customers make, the better the Services become. If\nCustomer sends us any feedback or suggestions regarding the Services, there\nis a chance we will use it, so Customer grants us (for itself and all of its\nAuthorized Users and other Customer personnel) an unlimited, irrevocable,\nperpetual, sublicensable, transferable, royalty-free license to use any such\nfeedback or suggestions for any purpose without any obligation or compensation\nto Customer, any Authorized User or other Customer personnel. If we choose\nnot to implement the suggestion, please don’t take it personally. We appreciate it\nnonetheless. </p>\n\n\n\n        <h5 class="TOSCategory">Disputes </h5>\n        <p>\n          If anyone brings a claim against us related to your actions, content or\ninformation on ListenUp, you will indemnify and hold us harmless from and\nagainst all damages, losses, and expenses of any kind (including\nreasonable legal fees and costs) related to such claim. Although we\nprovide rules for user conduct, we do not control or direct users\' actions on\nListenUp and are not responsible for the content or information users transmit\nor share on ListenUp. We are not responsible for any offensive, inappropriate,\nobscene, unlawful or otherwise objectionable content or information you\nmay encounter on ListenUp. We are not responsible for the conduct, whether\nonline or offline, of any user of ListenUp.\nWE TRY TO KEEP ListenUp UP, BUG-FREE, AND SAFE, BUT YOU USE IT\nAT YOUR OWN RISK. WE ARE PROVIDING ListenUp AS IS WITHOUT\nANY EXPRESS OR IMPLIED WARRANTIES INCLUDING, BUT NOT\nLIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. WE DO\nNOT GUARANTEE THAT ListenUp WILL ALWAYS BE SAFE, SECURE OR\nERROR-FREE OR THAT ListenUp WILL ALWAYS FUNCTION WITHOUT\nDISRUPTIONS, DELAYS OR IMPERFECTIONS. ListenUp IS NOT\nRESPONSIBLE FOR THE ACTIONS, CONTENT, INFORMATION, OR\nDATA OF THIRD PARTIES, AND YOU RELEASE US, OUR DIRECTORS,\nOFFICERS, EMPLOYEES, AND AGENTS FROM ANY CLAIMS AND\nDAMAGES, KNOWN AND UNKNOWN, ARISING OUT OF OR IN ANY\nWAY CONNECTED WITH ANY CLAIM YOU HAVE AGAINST ANY SUCH\nTHIRD PARTIES. NotedS\'S LIABILITY WILL BE LIMITED TO THE\nFULLEST EXTENT PERMITTED BY APPLICABLE LAW.\nSpecial Provisions Applicable to Users Outside the United States\nWe strive to create a global community with consistent standards for everyone,\nbut we also strive to respect local laws. The following provisions apply to users\nand non-users who interact with ListenUp outside the United States:\n• You consent to having your personal data transferred to and processed\nin the United States.\n        </p>\n          <h5 class="TOSCategory">Other </h5>\n        <p>This Statement is an agreement between you and ListenUp,\na product of Dreality LLC. References to “us,” “we,” and “our” mean either ListenUp,\na product of Dreality LLC. as appropriate.  </p>\n<p>\n• This Statement makes up the entire agreement between the parties\nregarding ListenUp, a product of Dreality LLC., and supersedes any prior agreements.\n</p>\n<p>• If any portion of this Statement is found to be unenforceable, the\nremaining portion will remain in full force and effect.\n</p>\n<p>• If we fail to enforce any of this Statement, it will not be considered a\nwaiver.</p>\n<p>• Any amendment to or waiver of this Statement must be made in writing\nand signed by us.\n</p>\n<p>• You will not transfer any of your rights or obligations under this\nStatement to anyone else without our consent.</p>\n<p>• All of our rights and obligations under this Statement are freely\nassignable by us in connection with a merger, acquisition,\nor sale of assets, or by operation of law or otherwise.</p>\n<p>• Nothing in this Statement shall prevent us from complying with the law.</p>\n<p>• This Statement does not confer any third party beneficiary rights.</p>\n<p>• We reserve all rights not expressly granted to you.</p>\n<p>• You will comply with all applicable laws when using or accessing ListenUp, a product of\nDreality LLC..</p>\n<p>\nBy using or accessing ListenUp Services, you agree that we can collect and use such\ncontent and information in accordance with the Privacy Policy as amended from\ntime to time.\n</p>\n\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/register/termsofservice-modal.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["o" /* ViewController */]])
    ], TermsOfServiceModal);
    return TermsOfServiceModal;
}());

//# sourceMappingURL=termsofservice-modal.js.map

/***/ }),

/***/ 23:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return UserInfoProvider; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3_firebase__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = y[op[0] & 2 ? "return" : op[0] ? "throw" : "next"]) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [0, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};




var UserInfoProvider = /** @class */ (function () {
    function UserInfoProvider(afAuth, afData) {
        this.afAuth = afAuth;
        this.afData = afData;
        console.log('Hello UserInfoProvider Provider');
    }
    //-----------------SET CURRENT USER'S INFORMATION--------------------
    UserInfoProvider.prototype.setUserInfo = function (user) {
        var _this = this;
        return this.afData.database.ref('users/' + user.uid).on('value', function (dataSnap) {
            _this.usrData = dataSnap.val();
            _this.usrId = user.uid;
            console.log("loaded current user: ", _this.usrData);
        });
    };
    UserInfoProvider.prototype.setUserInfoById = function (id) {
        var _this = this;
        return this.afData.database.ref('users/' + id).on('value', function (dataSnap) {
            _this.usrData = dataSnap.val();
            _this.usrId = id;
            console.log("loaded current user: ", _this.usrData);
        });
    };
    UserInfoProvider.prototype.clearUserInfo = function () {
        this.usrData = null;
        this.usrId = null;
    };
    //---------------ALL OF THE USERS---------------------------
    // async setUsers(){
    //    await this.afData.database.ref('users').once('value',dataSnap =>{
    //      this.usrGroup = dataSnap.val();
    //      console.log('All the users:',this.usrGroup);
    //      this.usrArray = [];
    //      for(var i in this.usrGroup){
    //  		this.usrArray.push(this.usrGroup[i]);
    //  	}
    //    })
    //    return this.usrArray
    //  }
    UserInfoProvider.prototype.setPhoto = function (id) {
        return __awaiter(this, void 0, void 0, function () {
            var _this = this;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, __WEBPACK_IMPORTED_MODULE_3_firebase__["storage"]().ref('profiles').child(id + '.jpg').getDownloadURL().then(function (success) {
                            _this.userPhoto = success;
                            _this.defaultBackground = true;
                        }, function (fail) {
                            _this.userPhoto = 'https://firebasestorage.googleapis.com/v0/b/eoko-cc928.appspot.com/o/profiles%2Fdefault_avatar.jpg?alt=media&token=761a4187-2508-44fb-994c-9bd0b6842181';
                            _this.defaultBackground = false;
                        })];
                    case 1:
                        _a.sent();
                        return [2 /*return*/];
                }
            });
        });
    };
    //LOAD OTHER PEOPLE INFORMATION
    UserInfoProvider.prototype.getOtherUserInfo = function (otherID) {
        var otherUser$ = this.afData.object("users/" + otherID).valueChanges();
        return otherUser$;
    };
    //----------------------ALL OF THE USERNAMES-------------------
    UserInfoProvider.prototype.setNameInfo = function () {
        return __awaiter(this, void 0, void 0, function () {
            var _this = this;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, this.afData.database.ref('usernames').on('value', function (dataSnap) {
                            _this.usrNames = dataSnap.val();
                        })];
                    case 1:
                        _a.sent();
                        return [2 /*return*/];
                }
            });
        });
    };
    //-----------------Getters-----------------
    UserInfoProvider.prototype.getUserInfo = function () {
        return this.usrData;
    };
    UserInfoProvider.prototype.getPhoto = function () {
        return this.userPhoto;
    };
    UserInfoProvider.prototype.getUserId = function () {
        return this.usrId;
    };
    UserInfoProvider.prototype.getDefault = function () {
        return this.defaultBackground;
    };
    // allUsers(){
    // 	return this.usrGroup;
    // }
    // usersArray(){
    // 	return this.usrArray;
    // }
    UserInfoProvider.prototype.getUserNames = function () {
        return this.usrNames;
    };
    UserInfoProvider = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_angularfire2_auth__["a" /* AngularFireAuth */], __WEBPACK_IMPORTED_MODULE_2_angularfire2_database__["a" /* AngularFireDatabase */]])
    ], UserInfoProvider);
    return UserInfoProvider;
}());

//# sourceMappingURL=userInfo.js.map

/***/ }),

/***/ 250:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return FeedbacktitlePage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
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
 * Generated class for the FeedbacktitlePage page.
 *d
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var FeedbacktitlePage = /** @class */ (function () {
    function FeedbacktitlePage(navCtrl, navParams) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.mesData = {
            title: "",
            message: ""
        };
        this.firstName = this.navParams.get('firstName');
        this.lastName = this.navParams.get('lastName');
        this.param = this.navParams.get('param');
        this.photoUrl = this.param.photourl;
        this.userName = this.param.username;
    }
    FeedbacktitlePage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad FeedbacktitlePage');
    };
    FeedbacktitlePage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-feedbacktitle',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/feedbacktitle/feedbacktitle.html"*/'<!--\n  Generated template for the FeedbacktitlePage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header >\n\n		<div class ="profile-blur" [style.background]="\'url(\'+ photoUrl +\')\'" ></div>\n\n		<ion-navbar color = "light" transparent>\n		</ion-navbar>\n	\n	<!-- profile pic -->\n	<h2 id = "profile-name"> Profile</h2>\n	<div class = "profile-container">\n\n			<img class="profile-pic" [src] = "photoUrl">\n		 <h1 class="profile-name">{{firstName}} {{lastName}}</h1>\n		 <p class = "username"> @{{userName}}</p>\n 	</div>\n\n</ion-header>\n<ion-content>\n\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/feedbacktitle/feedbacktitle.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */]])
    ], FeedbacktitlePage);
    return FeedbacktitlePage;
}());

//# sourceMappingURL=feedbacktitle.js.map

/***/ }),

/***/ 251:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ChatInfoProvider; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3_firebase__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = y[op[0] & 2 ? "return" : op[0] ? "throw" : "next"]) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [0, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
// import { HttpClient } from '@angular/common/http';




var ChatInfoProvider = /** @class */ (function () {
    function ChatInfoProvider(
        // public http: HttpClient
        afData, uInfo) {
        this.afData = afData;
        this.uInfo = uInfo;
        console.log('Hello ChatInfoProvider Provider');
    }
    //--------------------------------MESSAGE TAB ---------------------------------------------
    /**
     * [createNewChat initializes the chat object for that feedback ]
     * @param  {[string]} uid1       [first id]
     * @param  {[string]} uid2       [second id]
     * @param  {[string]} feedbackID [id of the feedback that is related to the chat]
     * @return {[type]}            [nothing]
     */
    ChatInfoProvider.prototype.createNewChat = function (uid1, uid2) {
        return __awaiter(this, void 0, void 0, function () {
            var ref, key, chatRef, uids, chatObj, userRef1, userRef2;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        ref = this.afData.database.ref("chats");
                        key = ref.push().key;
                        chatRef = ref.child(key);
                        uids = {};
                        uids[uid1] = {
                            id: uid1
                        };
                        uids[uid2] = {
                            id: uid2
                        };
                        chatObj = {
                            uids: uids,
                            key: key
                        };
                        return [4 /*yield*/, chatRef.update(chatObj)];
                    case 1:
                        _a.sent();
                        userRef1 = this.afData.database.ref("users/" + uid1 + "/chats/DMs/" + uid2);
                        userRef2 = this.afData.database.ref("users/" + uid2 + "/chats/DMs/" + uid1);
                        return [4 /*yield*/, userRef1.update({ chatID: key })];
                    case 2:
                        _a.sent();
                        return [4 /*yield*/, userRef2.update({ chatID: key })];
                    case 3:
                        _a.sent();
                        return [2 /*return*/, key];
                }
            });
        });
    };
    // Check if chat already exists, if yes returns the chat key, if no returns false
    // Returns a promise
    ChatInfoProvider.prototype.checkChat = function (uid1, uid2) {
        return __awaiter(this, void 0, void 0, function () {
            var chatRef, chatData;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        chatRef = __WEBPACK_IMPORTED_MODULE_3_firebase__["database"]().ref("users/" + uid1 + "/chats/DMs/" + uid2);
                        return [4 /*yield*/, chatRef.once("value")
                            //Check if chat has already existed
                        ];
                    case 1:
                        chatData = _a.sent();
                        //Check if chat has already existed
                        if (chatData.exists()) {
                            return [2 /*return*/, chatData.val().chatID];
                        }
                        else {
                            return [2 /*return*/, false];
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    ChatInfoProvider.prototype.enterChat = function (chatID) {
        var chatData = this.afData.list("chats/" + chatID).valueChanges();
        return chatData;
    };
    /**
     * loadChatData is different that loadMessages in that it loads data about the chat, while loadMessages load the messages from that chat
     * @param chatID
     * return data about the chat itself e.g. last text, timestamp, people in the chat
     */
    ChatInfoProvider.prototype.loadChatData = function (chatID) {
        var chatData$;
        chatData$ = this.afData.object("chats/" + chatID).valueChanges();
        return chatData$;
    };
    /**
     * [loadMessages loads the messages in an async list]
     * @param  {[string]} chatID [description]
     * @return {[Observable]}   messages$     [an Observable list of messages that is async]
     */
    ChatInfoProvider.prototype.loadMessages = function (chatID) {
        var messages$;
        messages$ = this.afData.list("messages/" + chatID + "/messages").valueChanges();
        return messages$;
    };
    //-------------------------------------CHAT TAB ---------------------------------------------------
    ChatInfoProvider.prototype.addMessage = function (text, userID, otherID, chatID) {
        return __awaiter(this, void 0, void 0, function () {
            var messageRef, key, timestamp, messageObj, chatRef, userRef, otherUserRef, obj;
            return __generator(this, function (_a) {
                messageRef = this.afData.database.ref("messages/" + chatID + "/messages");
                key = messageRef.push().key;
                timestamp = __WEBPACK_IMPORTED_MODULE_3_firebase__["database"].ServerValue.TIMESTAMP;
                messageObj = {
                    text: text,
                    timestamp: timestamp,
                    sender: userID,
                    receiver: otherID,
                    key: key
                };
                messageRef.child(key).update(messageObj);
                chatRef = this.afData.database.ref("chats/" + chatID);
                userRef = this.afData.database.ref("users/" + userID + "/chats/DMs/" + otherID);
                otherUserRef = this.afData.database.ref("users/" + otherID + "/chats/DMs/" + userID);
                console.log(userRef);
                obj = {
                    lastText: text,
                    timestamp: timestamp,
                    sender: userID,
                    receiver: otherID
                };
                chatRef.update(obj);
                userRef.update(obj);
                otherUserRef.update(obj);
                return [2 /*return*/];
            });
        });
    };
    ChatInfoProvider = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["A" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_2__userInfo_userInfo__["a" /* UserInfoProvider */]])
    ], ChatInfoProvider);
    return ChatInfoProvider;
}());

//# sourceMappingURL=chat-info.js.map

/***/ }),

/***/ 254:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return EditProfilePage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
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
 * Generated class for the EditProfilePage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var EditProfilePage = /** @class */ (function () {
    function EditProfilePage(navCtrl, navParams) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
    }
    EditProfilePage.prototype.ionViewDidLoad = function () {
        console.log('ionViewDidLoad EditProfilePage');
    };
    EditProfilePage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-edit-profile',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/modals/edit-profile/edit-profile.html"*/'<!--\n  Generated template for the EditProfilePage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n  <ion-navbar>\n    <ion-title>editProfile</ion-title>\n  </ion-navbar>\n\n</ion-header>\n\n\n<ion-content padding>\n  This is the edit profile modal\n\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/modals/edit-profile/edit-profile.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */]])
    ], EditProfilePage);
    return EditProfilePage;
}());

//# sourceMappingURL=edit-profile.js.map

/***/ }),

/***/ 255:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser_dynamic__ = __webpack_require__(256);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__app_module__ = __webpack_require__(274);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__ionic_native_http__ = __webpack_require__(100);



Object(__WEBPACK_IMPORTED_MODULE_0__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_1__app_module__["a" /* AppModule */]);
__WEBPACK_IMPORTED_MODULE_2__ionic_native_http__["a" /* HTTP */].getPluginRef = function () { return "cordova.plugin.http"; };
//# sourceMappingURL=main.js.map

/***/ }),

/***/ 274:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__ = __webpack_require__(33);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__ionic_native_splash_screen__ = __webpack_require__(248);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__ionic_native_status_bar__ = __webpack_require__(249);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__ionic_native_barcode_scanner__ = __webpack_require__(253);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_angularfire2__ = __webpack_require__(38);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__app_component__ = __webpack_require__(384);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__app_firebase_config__ = __webpack_require__(385);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__ionic_native_linkedin__ = __webpack_require__(206);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__ionic_native_in_app_browser__ = __webpack_require__(207);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__pages_tabs_tabs__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__pages_login_login__ = __webpack_require__(65);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__pages_register_register__ = __webpack_require__(124);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__pages_createuser_createuser__ = __webpack_require__(66);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__pages_blockusers_blockusers__ = __webpack_require__(123);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__components_components_module__ = __webpack_require__(386);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_19__pages_register_termsofservice_modal__ = __webpack_require__(205);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_20__modals_edit_profile_edit_profile__ = __webpack_require__(254);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_21__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_22__ionic_native_camera__ = __webpack_require__(252);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_23__pages_feedbacktitle_feedbacktitle__ = __webpack_require__(250);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_24__pipes_pipes_module__ = __webpack_require__(388);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_25__providers_chat_info_chat_info__ = __webpack_require__(251);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_26__ionic_storage__ = __webpack_require__(391);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_27__angular_http__ = __webpack_require__(204);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_28__angular_common_http__ = __webpack_require__(208);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_29__ionic_native_http__ = __webpack_require__(100);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
















// import {SendfeedPage} from '../pages/sendfeed/sendfeed';
// import {SearchuserPage} from '../pages/searchuser/searchuser';



// import {SettingsPage} from '../pages/settings/settings';
//Import Modal








// import { IonicImageLoader } from 'ionic-image-loader';



var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_1__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_8__app_component__["a" /* MyApp */],
                // FeedbackPage,
                // MessagePage,
                // ProfilePage,
                __WEBPACK_IMPORTED_MODULE_15__pages_register_register__["a" /* RegisterPage */],
                __WEBPACK_IMPORTED_MODULE_13__pages_tabs_tabs__["a" /* TabsPage */],
                __WEBPACK_IMPORTED_MODULE_14__pages_login_login__["a" /* LoginPage */],
                __WEBPACK_IMPORTED_MODULE_23__pages_feedbacktitle_feedbacktitle__["a" /* FeedbacktitlePage */],
                // SendfeedPage,
                // SearchuserPage,
                __WEBPACK_IMPORTED_MODULE_16__pages_createuser_createuser__["a" /* CreateuserPage */],
                __WEBPACK_IMPORTED_MODULE_17__pages_blockusers_blockusers__["a" /* BlockusersPage */],
                // SettingsPage,
                // TermsOfServicesPage,
                __WEBPACK_IMPORTED_MODULE_19__pages_register_termsofservice_modal__["a" /* TermsOfServiceModal */],
                __WEBPACK_IMPORTED_MODULE_20__modals_edit_profile_edit_profile__["a" /* EditProfilePage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__["a" /* BrowserModule */],
                __WEBPACK_IMPORTED_MODULE_27__angular_http__["c" /* HttpModule */],
                __WEBPACK_IMPORTED_MODULE_28__angular_common_http__["b" /* HttpClientModule */],
                __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["f" /* IonicModule */].forRoot(__WEBPACK_IMPORTED_MODULE_8__app_component__["a" /* MyApp */], {
                    mode: 'ios',
                    iconMode: 'ios',
                    backButtonText: ''
                }, {
                    links: [
                        { loadChildren: '../pages/blockusers/blockusers.module#BlockusersPageModule', name: 'BlockusersPage', segment: 'blockusers', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/createuser/createuser.module#CreateuserPageModule', name: 'CreateuserPage', segment: 'createuser', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/feedbacktitle/feedbacktitle.module#FeedbacktitlePageModule', name: 'FeedbacktitlePage', segment: 'feedbacktitle', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/message-detail/message-detail.module#MessageDetailPageModule', name: 'MessageDetailPage', segment: 'message-detail', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/message/message.module#MessagePageModule', name: 'MessagePage', segment: 'message', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/profile/profile.module#ProfilePageModule', name: 'ProfilePage', segment: 'profile', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/register/register.module#RegisterPageModule', name: 'RegisterPage', segment: 'register', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/searchuser/searchuser.module#SearchuserPageModule', name: 'SearchuserPage', segment: 'searchuser', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/settings/settings.module#SettingsPageModule', name: 'SettingsPage', segment: 'settings', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/feedback/feedback.module#FeedbackPageModule', name: 'FeedbackPage', segment: 'feedback', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/login/login.module#LoginPageModule', name: 'LoginPage', segment: 'login', priority: 'low', defaultHistory: [] },
                        { loadChildren: '../pages/sendfeed/sendfeed.module#SendfeedPageModule', name: 'SendfeedPage', segment: 'sendfeed', priority: 'low', defaultHistory: [] }
                    ]
                }),
                __WEBPACK_IMPORTED_MODULE_6_angularfire2__["a" /* AngularFireModule */].initializeApp(__WEBPACK_IMPORTED_MODULE_9__app_firebase_config__["a" /* FIREBASE_CONFIG */]),
                __WEBPACK_IMPORTED_MODULE_12_angularfire2_database__["b" /* AngularFireDatabaseModule */],
                __WEBPACK_IMPORTED_MODULE_24__pipes_pipes_module__["a" /* PipesModule */],
                __WEBPACK_IMPORTED_MODULE_18__components_components_module__["a" /* ComponentsModule */],
                __WEBPACK_IMPORTED_MODULE_26__ionic_storage__["a" /* IonicStorageModule */].forRoot(),
            ],
            bootstrap: [__WEBPACK_IMPORTED_MODULE_2_ionic_angular__["d" /* IonicApp */]],
            entryComponents: [
                __WEBPACK_IMPORTED_MODULE_8__app_component__["a" /* MyApp */],
                __WEBPACK_IMPORTED_MODULE_15__pages_register_register__["a" /* RegisterPage */],
                __WEBPACK_IMPORTED_MODULE_13__pages_tabs_tabs__["a" /* TabsPage */],
                __WEBPACK_IMPORTED_MODULE_23__pages_feedbacktitle_feedbacktitle__["a" /* FeedbacktitlePage */],
                // SendfeedPage,
                // SearchuserPage,
                __WEBPACK_IMPORTED_MODULE_16__pages_createuser_createuser__["a" /* CreateuserPage */],
                __WEBPACK_IMPORTED_MODULE_17__pages_blockusers_blockusers__["a" /* BlockusersPage */],
                __WEBPACK_IMPORTED_MODULE_14__pages_login_login__["a" /* LoginPage */],
                // SettingsPage,
                // TermsOfServicesPage,
                __WEBPACK_IMPORTED_MODULE_19__pages_register_termsofservice_modal__["a" /* TermsOfServiceModal */],
                __WEBPACK_IMPORTED_MODULE_20__modals_edit_profile_edit_profile__["a" /* EditProfilePage */],
            ],
            providers: [
                __WEBPACK_IMPORTED_MODULE_4__ionic_native_status_bar__["a" /* StatusBar */],
                __WEBPACK_IMPORTED_MODULE_3__ionic_native_splash_screen__["a" /* SplashScreen */],
                { provide: __WEBPACK_IMPORTED_MODULE_1__angular_core__["u" /* ErrorHandler */], useClass: __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["e" /* IonicErrorHandler */] },
                __WEBPACK_IMPORTED_MODULE_7_angularfire2_auth__["a" /* AngularFireAuth */],
                __WEBPACK_IMPORTED_MODULE_12_angularfire2_database__["b" /* AngularFireDatabaseModule */],
                __WEBPACK_IMPORTED_MODULE_21__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
                // SearchuserPage,
                __WEBPACK_IMPORTED_MODULE_22__ionic_native_camera__["a" /* Camera */],
                __WEBPACK_IMPORTED_MODULE_25__providers_chat_info_chat_info__["a" /* ChatInfoProvider */],
                __WEBPACK_IMPORTED_MODULE_5__ionic_native_barcode_scanner__["a" /* BarcodeScanner */],
                __WEBPACK_IMPORTED_MODULE_10__ionic_native_linkedin__["a" /* LinkedIn */],
                __WEBPACK_IMPORTED_MODULE_11__ionic_native_in_app_browser__["a" /* InAppBrowser */],
                __WEBPACK_IMPORTED_MODULE_29__ionic_native_http__["a" /* HTTP */],
            ]
        })
    ], AppModule);
    return AppModule;
}());

//# sourceMappingURL=app.module.js.map

/***/ }),

/***/ 384:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return MyApp; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__ionic_native_status_bar__ = __webpack_require__(249);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__ionic_native_splash_screen__ = __webpack_require__(248);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__pages_tabs_tabs__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__pages_login_login__ = __webpack_require__(65);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__pages_createuser_createuser__ = __webpack_require__(66);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};









var MyApp = /** @class */ (function () {
    function MyApp(platform, statusBar, splashScreen, afAuth, uInfo) {
        var _this = this;
        this.afAuth = afAuth;
        this.uInfo = uInfo;
        this.loadUserInfo();
        platform.ready().then(function () {
            _this.afAuth.auth.onAuthStateChanged(function (user) {
                if (user) {
                    _this.uInfo.setUserInfo(user);
                    _this.loadUserInfo();
                    _this.uInfo.setNameInfo();
                }
                else {
                    _this.rootPage = __WEBPACK_IMPORTED_MODULE_5__pages_login_login__["a" /* LoginPage */];
                }
                console.log("auth state", user);
            });
            statusBar.styleDefault();
            splashScreen.hide();
        });
    }
    MyApp.prototype.loadUserInfo = function () {
        var _this = this;
        this.usrInfo = this.uInfo.getUserInfo();
        if (this.usrInfo) {
            this.uInfo.setPhoto(this.usrInfo.id);
        }
        if (this.usrInfo == undefined || this.uInfo.getPhoto() == undefined) {
            setTimeout(function () {
                _this.loadUserInfo();
            }, 1000);
        }
        else {
            if (this.usrInfo.username) {
                this.rootPage = __WEBPACK_IMPORTED_MODULE_4__pages_tabs_tabs__["a" /* TabsPage */];
            }
            else {
                this.rootPage = __WEBPACK_IMPORTED_MODULE_8__pages_createuser_createuser__["a" /* CreateuserPage */];
            }
        }
    };
    MyApp = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/app/app.html"*/'<ion-menu [content] = "content" >\n	<ion-header>\n		<ion-toolbar >\n		</ion-toolbar>\n	</ion-header>\n	<ion-content>\n		<header-menu></header-menu>\n	</ion-content>\n</ion-menu>\n<ion-nav [root]="rootPage" #content></ion-nav>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/app/app.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["m" /* Platform */], __WEBPACK_IMPORTED_MODULE_2__ionic_native_status_bar__["a" /* StatusBar */],
            __WEBPACK_IMPORTED_MODULE_3__ionic_native_splash_screen__["a" /* SplashScreen */], __WEBPACK_IMPORTED_MODULE_6_angularfire2_auth__["a" /* AngularFireAuth */], __WEBPACK_IMPORTED_MODULE_7__providers_userInfo_userInfo__["a" /* UserInfoProvider */]])
    ], MyApp);
    return MyApp;
}());

//# sourceMappingURL=app.component.js.map

/***/ }),

/***/ 385:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return FIREBASE_CONFIG; });
var FIREBASE_CONFIG = {
    apiKey: "AIzaSyBXwSOIndLWBqKIlQlzhn2CZAuUWgfAwOw",
    authDomain: "listenuptesting.firebaseapp.com",
    databaseURL: "https://listenuptesting.firebaseio.com",
    projectId: "listenuptesting",
    storageBucket: "listenuptesting.appspot.com",
    messagingSenderId: "319406214050"
};
// "AIzaSyD3U0uJvjBydi8hOrPjqZx2gX8BHrgnPuw",
//     authDomain: "feedbackloop-66067.firebaseapp.com",
//     databaseURL: "https://feedbackloop-66067.firebaseio.com",
//     projectId: "feedbackloop-66067",
//     storageBucket: "feedbackloop-66067.appspot.com",
//     messagingSenderId: "699957173171" 
//# sourceMappingURL=app.firebase.config.js.map

/***/ }),

/***/ 386:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ComponentsModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__header_menu_header_menu__ = __webpack_require__(387);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_ionic_angular__ = __webpack_require__(10);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var ComponentsModule = /** @class */ (function () {
    function ComponentsModule() {
    }
    ComponentsModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [__WEBPACK_IMPORTED_MODULE_1__header_menu_header_menu__["a" /* HeaderMenuComponent */]],
            imports: [__WEBPACK_IMPORTED_MODULE_2_ionic_angular__["f" /* IonicModule */]],
            exports: [__WEBPACK_IMPORTED_MODULE_1__header_menu_header_menu__["a" /* HeaderMenuComponent */]]
        })
    ], ComponentsModule);
    return ComponentsModule;
}());

//# sourceMappingURL=components.module.js.map

/***/ }),

/***/ 387:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return HeaderMenuComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__pages_login_login__ = __webpack_require__(65);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__pages_blockusers_blockusers__ = __webpack_require__(123);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};








// import{SettingsPage} from "../../pages/settings/settings";
/**
 * Generated class for the HeaderMenuComponent component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
var HeaderMenuComponent = /** @class */ (function () {
    function HeaderMenuComponent(afAuth, menuCtrl, app, afData, uInfo, alertCtrl) {
        this.afAuth = afAuth;
        this.menuCtrl = menuCtrl;
        this.app = app;
        this.afData = afData;
        this.uInfo = uInfo;
        this.alertCtrl = alertCtrl;
        this.blockedUsers = [];
        this.blockedObj = {};
        console.log('Hello HeaderMenuComponent Component');
        this.text = 'Hello World';
        this.loadUserInfo();
        //this.blocked();
    }
    HeaderMenuComponent.prototype.loadUserInfo = function () {
        var _this = this;
        this.usrInfo = this.uInfo.getUserInfo();
        if (this.usrInfo == undefined) {
            console.log("try again on header menu page");
            setTimeout(function () {
                _this.loadUserInfo();
            }, 1000);
        }
        else {
            console.log("success loading in userinfo");
            this.annonStatus = this.uInfo.getUserInfo().allowAnnon;
        }
    };
    HeaderMenuComponent.prototype.blocked = function () {
        //   for(var i in this.usrInfo.blocked){
        //     var unique = true;
        //     for(var j in this.blockedUsers){
        //       if(this.usrInfo.blockedusers[i] == this.blockedUsers[j]){
        //         unique = false;
        //       }
        //     }
        //     if(this.usrInfo.blockedusers[i] != "annonymous" && unique ){
        //       this.blockedObj[i] = this.usrInfo.blockedusers[i];
        //         this.blockedUsers.push(this.usrInfo.blockedusers[i]);
        //       }
        //   }
        // console.log("blocked users");
        this.menuCtrl.close();
        var nav = this.app.getRootNav();
        nav.push(__WEBPACK_IMPORTED_MODULE_6__pages_blockusers_blockusers__["a" /* BlockusersPage */] /*,{param1:this.blockedObj,param: this.blockedUsers}*/);
        //this.navCtrl.push(BlockusersPage,{param:this.blockedUsers});
    };
    HeaderMenuComponent.prototype.allowAnnon = function () {
        if (this.annonStatus) {
            this.afData.database.ref('users').child(this.uInfo.getUserId()).update({ allowAnnon: true });
            //this.annonStatus = false
            console.log("disabled annon");
        }
        else {
            this.afData.database.ref('users').child(this.uInfo.getUserId()).update({ allowAnnon: false });
            console.log("enabled annon");
            //this.annonStatus = true
        }
    };
    HeaderMenuComponent.prototype.logoutClicked = function () {
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
                        nav.setRoot(__WEBPACK_IMPORTED_MODULE_2__pages_login_login__["a" /* LoginPage */]);
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
    HeaderMenuComponent.prototype.pushSettings = function () {
        var nav = this.app.getRootNav();
        this.menuCtrl.close();
        nav.setRoot("SettingsPage");
    };
    HeaderMenuComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'header-menu',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/components/header-menu/header-menu.html"*/'<!-- Generated template for the HeaderMenuComponent component -->\n<div class = "listItem" > \n  <ion-list >\n<!--   	<ion-item (click) = "blocked()" ><ion-icon name = "ios-close-circle-outline"> </ion-icon> Blocked Users</ion-item> -->\n\n<!--   	<ion-item >\n  		<ion-label><ion-icon name= "ios-contacts"> </ion-icon> Anonymous Feedback </ion-label> 	\n  		<ion-toggle [(ngModel)] = "annonStatus" (ngModelChange) = "allowAnnon($event)"></ion-toggle> \n  	</ion-item > -->\n   \n    <ion-item (click)="pushSettings()" >\n      <ion-label><ion-icon name = "ios-settings-outline"> </ion-icon>  Settings</ion-label>   \n    </ion-item >\n\n\n<!--     <ion-item >\n      <ion-label><ion-icon name = "ios-create-outline"> </ion-icon> Sent Feedbacks</ion-label>   \n    </ion-item >\n -->\n\n    <ion-item >\n      <ion-label><ion-icon name = "ios-folder-open-outline"> </ion-icon> Saved/Sent Feedbacks</ion-label>   \n    </ion-item >\n\n<!--     <ion-item >\n      <ion-label><ion-icon name = "ios-call-outline"> </ion-icon> Contact Support</ion-label>   \n    </ion-item > -->\n\n<!--     <ion-item >\n      <ion-label><ion-icon name = "ios-barcode-outline"> </ion-icon> QR Code</ion-label>   \n    </ion-item >\n -->\n    <ion-item >\n      <ion-label><ion-icon name = "ios-person-add-outline"> </ion-icon> Invite Friends</ion-label>   \n    </ion-item >\n\n    <ion-item >\n      <ion-label><ion-icon name = "ios-pricetag-outline"> </ion-icon> Upgrade to Pro</ion-label>   \n    </ion-item >\n\n    <ion-item (click) = "logoutClicked();">\n      <ion-label><ion-icon name = "ios-log-out-outline" > </ion-icon> Log Out</ion-label> \n    </ion-item >\n    <!-- <ion-item no-lines >\n      Contact Developers:  \n    </ion-item>\n    <ion-item >\n        <span id = "email">drealityllc@gmail.com</span>\n    </ion-item> -->\n    <!-- <ion-item *ngIf = "annonStatus">\n      <ion-label> Block Annon Feedback</ion-label>  \n      <ion-toggle [(ngModel)] = "annonStatus" (ngModelChange) = "allowAnnon($event)" checked = "false"></ion-toggle> \n    </ion-item> -->\n \n\n  </ion-list>\n</div>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/components/header-menu/header-menu.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_angularfire2_auth__["a" /* AngularFireAuth */],
            __WEBPACK_IMPORTED_MODULE_3_ionic_angular__["i" /* MenuController */],
            __WEBPACK_IMPORTED_MODULE_3_ionic_angular__["c" /* App */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_5__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_3_ionic_angular__["b" /* AlertController */]])
    ], HeaderMenuComponent);
    return HeaderMenuComponent;
}());

//# sourceMappingURL=header-menu.js.map

/***/ }),

/***/ 388:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return PipesModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__sort_by_sort_by__ = __webpack_require__(389);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__objto_array_objto_array__ = __webpack_require__(390);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var PipesModule = /** @class */ (function () {
    function PipesModule() {
    }
    PipesModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [__WEBPACK_IMPORTED_MODULE_1__sort_by_sort_by__["a" /* SortByPipe */],
                __WEBPACK_IMPORTED_MODULE_2__objto_array_objto_array__["a" /* ObjtoArrayPipe */]],
            imports: [],
            exports: [__WEBPACK_IMPORTED_MODULE_1__sort_by_sort_by__["a" /* SortByPipe */],
                __WEBPACK_IMPORTED_MODULE_2__objto_array_objto_array__["a" /* ObjtoArrayPipe */]]
        })
    ], PipesModule);
    return PipesModule;
}());

//# sourceMappingURL=pipes.module.js.map

/***/ }),

/***/ 389:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SortByPipe; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var SortByPipe = /** @class */ (function () {
    function SortByPipe() {
    }
    SortByPipe.prototype.transform = function (array, stringArray) {
        var path = stringArray[0];
        var direction = stringArray[1];
        if (array == null) {
            return null;
        }
        if (direction == 'smallest') {
            array.sort(function (a, b) {
                if (a[path] < b[path]) {
                    //a is the Object and args is the orderBy condition (data.likes.count in this case)
                    return -1;
                }
                else if (a[path] > b[path]) {
                    return 1;
                }
                else {
                    return 0;
                }
            });
        }
        if (direction == 'largest') {
            array.sort(function (a, b) {
                if (a[path] < b[path]) {
                    //a is the Object and args is the orderBy condition (data.likes.count in this case)
                    return 1;
                }
                else if (a[path] > b[path]) {
                    return -1;
                }
                else {
                    return 0;
                }
            });
        }
        return array;
    };
    SortByPipe = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["S" /* Pipe */])({
            name: 'sortBy',
        })
    ], SortByPipe);
    return SortByPipe;
}());

//# sourceMappingURL=sort-by.js.map

/***/ }),

/***/ 390:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ObjtoArrayPipe; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var ObjtoArrayPipe = /** @class */ (function () {
    function ObjtoArrayPipe() {
    }
    ObjtoArrayPipe.prototype.transform = function (obj) {
        var result = [];
        for (var i in obj) {
            result.push(obj[i]);
        }
        return result;
    };
    ObjtoArrayPipe = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["S" /* Pipe */])({
            name: 'objtoArray',
        })
    ], ObjtoArrayPipe);
    return ObjtoArrayPipe;
}());

//# sourceMappingURL=objto-array.js.map

/***/ }),

/***/ 59:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TabsPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var TabsPage = /** @class */ (function () {
    function TabsPage() {
        this.tab1Root = "ProfilePage";
        this.tab2Root = "FeedbackPage";
        this.tab3Root = "MessagePage";
    }
    TabsPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/tabs/tabs.html"*/'<ion-tabs background-color = "primary" selectedIndex="1">\n  <ion-tab [root]="tab1Root" tabTitle="Profile" tabIcon="ios-person" color = "primary"></ion-tab>\n  <ion-tab [root]="tab2Root" tabTitle="MyFeedback" tabIcon="md-funnel" color = "primary"></ion-tab>\n  <ion-tab [root]="tab3Root" tabTitle="Messages" tabIcon="ios-chatbubbles" color = "primary"></ion-tab>\n</ion-tabs>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/tabs/tabs.html"*/
        }),
        __metadata("design:paramtypes", [])
    ], TabsPage);
    return TabsPage;
}());

//# sourceMappingURL=tabs.js.map

/***/ }),

/***/ 65:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return LoginPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_http__ = __webpack_require__(204);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__tabs_tabs__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__register_register__ = __webpack_require__(124);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__ionic_native_linkedin__ = __webpack_require__(206);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_firebase_app__ = __webpack_require__(96);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_firebase_app___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_8_firebase_app__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__ionic_native_in_app_browser__ = __webpack_require__(207);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__angular_common_http__ = __webpack_require__(208);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__ionic_native_http__ = __webpack_require__(100);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12_rxjs_add_operator_map__ = __webpack_require__(58);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12_rxjs_add_operator_map___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_12_rxjs_add_operator_map__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = y[op[0] & 2 ? "return" : op[0] ? "throw" : "next"]) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [0, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};








//import * as firebase from 'firebase';








// import {Injectable} from '@angular/core';
// import 'rxjs/add/operator/map';
/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
// @Injectable()
var LoginPage = /** @class */ (function () {
    function LoginPage(afAuth, navCtrl, navParams, platform, uInfo, menuCtrl, linkedin, http, inApp, load, httpPlug, alertCtrl, httpClient) {
        this.afAuth = afAuth;
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.platform = platform;
        this.uInfo = uInfo;
        this.menuCtrl = menuCtrl;
        this.linkedin = linkedin;
        this.http = http;
        this.inApp = inApp;
        this.load = load;
        this.httpPlug = httpPlug;
        this.alertCtrl = alertCtrl;
        this.httpClient = httpClient;
        this.log = false;
        this.reg = false;
        this.rootPage = LoginPage_1;
        this.user = {};
        this.scopes = ['r_basicprofile', 'r_emailaddress'];
        this.testingBool = false;
        this.linkedinUri = "https://www.linkedin.com/oauth/v2/authorization?format=json&response_type=code&client_id=7818gxiruyce0r&redirect_uri=http://localhost:8100/callback&state=Listenuptesting&r_basicprofile%20r_emailaddress";
        this.apiUrl = 'https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken';
        // serviceAccount = require();
        this.selfData = { id: "", firstName: "", lastName: "" };
        this.menuCtrl.swipeEnable(false);
    }
    LoginPage_1 = LoginPage;
    LoginPage.prototype.login = function (user) {
        return __awaiter(this, void 0, void 0, function () {
            var result, e_1;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        this.log = true;
                        _a.label = 1;
                    case 1:
                        _a.trys.push([1, 3, , 4]);
                        return [4 /*yield*/, this.afAuth.auth.signInWithEmailAndPassword(user.email, user.password)];
                    case 2:
                        result = _a.sent();
                        if (result) {
                            console.log('result', result);
                            this.loadUserInfo();
                            this.navCtrl.setRoot(__WEBPACK_IMPORTED_MODULE_4__tabs_tabs__["a" /* TabsPage */]);
                        }
                        return [3 /*break*/, 4];
                    case 3:
                        e_1 = _a.sent();
                        console.error(e_1);
                        return [3 /*break*/, 4];
                    case 4: return [2 /*return*/];
                }
            });
        });
    };
    // linkedInlLogin(){
    //    this.linkedin.login(this.scopes, true)
    //     .then(() => console.log('Logged in!'))
    //     .catch(e => console.log('Error logging in', e));
    // }
    LoginPage.prototype.askCloud = function (id) {
        var url = "https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken";
        var params = new URLSearchParams();
        // let headers = new Headers({'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' });
        params.set('linkedin', id);
        return this.http.post(url, params)
            .toPromise()
            .then(function (res) {
            console.log(res);
        })
            .catch(function (err) {
            console.log(err);
        });
    };
    LoginPage.prototype.linkedLogin = function () {
        var _this = this;
        this.linkedin.login(this.scopes, true)
            .then(function (success) {
            console.log("success time", success);
            _this.isLoggedIn = true;
            _this.getSelfData();
            _this.linkedin.getActiveSession().then(function (token) {
                _this.accessToken = token;
            });
        })
            .catch(function (e) { return console.log('Error logging in', e); });
    };
    // linkedInLogin(){
    //   let browserRef = window.open(this.linkedinUri, '_blank', 'location=no');
    //     browserRef.addEventListener("?code=", (event: any) => {
    //       if ((event.url).indexOf('?code=') !== -1) {
    //         let token = event.url.slice(event.url.indexOf('?code=') + '?code='.length);
    //         // here is your token, now you can close the InAppBrowser
    //         browserRef.close();
    //         console.log("token is",token);
    //       }
    //     })
    //   // this.http.get('').subscribe((data) => {
    //   //   console.log("data",data.text())
    //   // })
    // }
    LoginPage.prototype.getLinkCode = function () {
        var inApp = this.inApp;
        var linkedinUri = this.linkedinUri;
        var load = this.load;
        var headers = new __WEBPACK_IMPORTED_MODULE_0__angular_http__["a" /* Headers */]();
        headers.append('Content-Type', 'application/x-www-form-urlencoded');
        headers.append('Host', 'www.linkedin.com');
        var options = new __WEBPACK_IMPORTED_MODULE_0__angular_http__["d" /* RequestOptions */]({
            headers: headers
        });
        var http = this.http;
        return new Promise(function (resolve, reject) {
            var browserRef = window.open(linkedinUri, "_blank", "location=no,clearsessioncache=yes,clearcache=yes");
            browserRef.addEventListener("loadstart", function (event) {
                if ((event.url).indexOf("localhost:8100/callback") === 0) {
                    browserRef.removeEventListener("exit", function (event) { });
                    browserRef.close();
                    console.log("EVENT", event.url);
                    //                 if ((event.url).indexOf('?code=') !== -1) {
                    //                         let code = event.url.slice(event.url.indexOf('?code=') + '?code='.length);
                    //                         let arrayCode = code.split('&')
                    //                         console.log("BIG CODE",arrayCode[0]);
                    //                         console.log('CHECKING GOOD',arrayCode[1]);
                    //                         var content = "grand_type=authorization_code&code=" + arrayCode[0] + "&redirect_uri=http://localhost:8100/callback&client_id=7818gxiruyce0r&client_secret=gGmAzVSZ1C1Qlws2"
                    //                         http.post("/oauth/v2/accessToken",content,options).toPromise().then(res => {
                    //                         let result = res.json();
                    //                         console.log("BIG RESULTS",result);
                    // })
                    // }
                    console.log("event.url 2 -> " + event.url);
                    var parsedResponse = {};
                    var code = (event.url.split("=")[1]).split("&")[0];
                    var state = event.url.split("=")[2];
                    if (code !== undefined && state !== null) {
                        console.log("code : " + code + "  state : " + state);
                        parsedResponse["code"] = code;
                        //parsedResponse["state"] = state;
                        resolve(parsedResponse);
                    }
                    else {
                        reject("Problem authenticating with LinkedIn");
                    }
                }
            });
            browserRef.addEventListener("exit", function (event) {
                reject("The Facebook sign in flow was canceled");
            });
        });
    };
    LoginPage.prototype.getToken = function (code) {
        var headers = new __WEBPACK_IMPORTED_MODULE_0__angular_http__["a" /* Headers */]({
            "Content-Type": 'application/x-www-form-urlencoded'
        });
        var options = new __WEBPACK_IMPORTED_MODULE_0__angular_http__["d" /* RequestOptions */]({
            headers: headers,
        });
        var dat = {
            grant_type: "authorization_code",
            code: code.code,
            redirect_uri: 'http://localhost:8100/callback',
            client_id: '7818gxiruyce0r',
            client_secret: 'gGmAzVSZ1C1Qlws2'
        };
        var newDat = JSON.stringify(dat);
        return this.http.post("https://www.linkedin.com/oauth/v2/accessToken", newDat, options)
            .map(function (res) { return res.json(); });
    };
    LoginPage.prototype.linkedInLogin = function () {
        var _this = this;
        var loader;
        this.platform.ready().then(function () { return _this.getLinkCode().then(function (success) {
            console.log("SUccess" + success.code);
            // console.log("Tokenworks",this.getToken(success));
            // let headers = new Headers({
            //   "Content-Type": 'application/x-www-form-urlencoded'
            // });
            // let options = new RequestOptions({
            //   headers: headers,
            // });
            var data = "grant_type=authorization_code&code=" + success.code + "&redirect_uri=http://localhost:8100/callback&client_id=7818gxiruyce0r&client_secret=gGmAzVSZ1C1Qlws2";
            //     this.http.post("https://www.linkedin.com/oauth/v2/accessToken",data).toPromise().then(success => {
            //          console.log("lucian",success);
            //     },
            //     fail => {
            //       console.log("FAILURE",fail);
            //     }
            //     );
            // this.httpClient.post("https://www.linkedin.com/oauth/v2/accessToken",data,{headers:{"Content-Type":"application/x-www-form-urlencoded"}}).toPromise().then( success => {
            //   console.log("successful",success);
            // },
            // fail => {
            //   console.log("failure",fail);
            // }
            // )
            // this.http.post('https://www.linkedin.com/oauth/v2/accessToken',body,options).toPromise().then(res =>{ 
            //    let result = res.json();
            //    console.log("fuck",result);
            //  })
            // this.http.post('https://www.linkedin.com/oauth/v2/accessToken', dat,{})
            // this.httpPlug.setHeader("www.linkedin.com","Content-Type","application/x-www-form-urlencoded");
            var dat = {
                grant_type: "authorization_code",
                code: success,
                redirect_uri: 'redirect_uri=http://localhost:8100/callback',
                client_id: '7818gxiruyce0r',
                client_secret: 'gGmAzVSZ1C1Qlws2'
            };
            _this.httpPlug.setDataSerializer('urlencoded');
            _this.httpPlug.post("https://www.linkedin.com/oauth/v2/accessToken", dat, { "Content-Type": "application/x-www-form-urlencoded" }).then(function (res) {
                var result = res;
                if (result) {
                    _this.testingBool = true;
                }
                _this.testingInfo = result;
                console.log("http result:", result);
            }, function (fail) {
                console.log("FAILURE", fail);
            });
        }); });
    };
    // getLinkedInUserDetails(token: string) {
    //     let headers = new Headers({
    //       'Content-Type': 'application/x-www-form-urlencoded',
    //       'Authorization': 'Bearer ' + token//,
    //     });
    //     let options = new RequestOptions({
    //       headers: headers,
    //     });
    //     var data: any;
    //     data = 
    //     return this.http.get("https://api.linkedin.com/v1/people/~:(id,first-name,last-name,email-address,picture-url)?format=json", options).toPromise()
    //       .then(res => res.json(), err => err);
    //   }
    // firebaselogin(){
    //   firebase.auth().getRedirectResult().then(function(result) {
    //   if (result.credential) {
    //     // This gives you the OAuth Access Token for that provider.
    //     var token = result.credential.accessToken;
    //   }
    //   var user = result.user;
    // });
    // // Start a sign in process for an unauthenticated user.
    // var provider =  new firebase.auth.OAuthProvider('linkedin.com');
    // provider.addScope('r_basicprofile');
    // provider.addScope('r_emailaddress');
    // firebase.auth().signInWithRedirect(provider);
    // }
    LoginPage.prototype.loadUserInfo = function () {
        var _this = this;
        this.usrInfo = this.uInfo.getUserInfo();
        if (this.usrInfo == undefined || this.usrInfo == null) {
            setTimeout(function () {
                _this.loadUserInfo();
            }, 1000);
        }
    };
    LoginPage.prototype.getSelfData = function () {
        var _this = this;
        this.linkedin.getRequest('people/~')
            .then(function (res) {
            _this.selfData = res;
            console.log("DATA TIME BITCHES", res);
            var token = _this.askCloud(res.id);
        })
            .catch(function (e) { return console.log(e); });
    };
    LoginPage.prototype.ionViewDidAppear = function () {
        var _this = this;
        this.linkedin.hasActiveSession().then(function (active) {
            _this.isLoggedIn = active;
            if (_this.isLoggedIn === true) {
                _this.getSelfData();
            }
        });
    };
    LoginPage.prototype.signInWithToken = function (token) {
        __WEBPACK_IMPORTED_MODULE_8_firebase_app__["auth"]().signInWithCustomToken(token).catch(function (error) {
            var errorCode = error.code;
            var errorMessage = error.message;
        });
    };
    LoginPage.prototype.createToken = function (id) {
        // this.http.get('https://us-central1-listenuptesting.cloudfunctions.net/createFirebaseToken?id=' + id).subscribe((data) => {
        //   console.log("data",data.text());
        //   this.signInWithToken(data.text());
        // })
        this.signInWithToken('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJyNTE1eSIsImlhdCI6MTUzMTYzNzM4OSwiZXhwIjoxNTMxNjQwOTg5LCJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlzcyI6ImZpcmViYXNlLWFkbWluc2RrLW5oY2phQGxpc3RlbnVwdGVzdGluZy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsInN1YiI6ImZpcmViYXNlLWFkbWluc2RrLW5oY2phQGxpc3RlbnVwdGVzdGluZy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSJ9.FfZk49OiOr6NGQxuair6LZY-Hih6gJgnjAV2oAXojp30cQTbzVqdcySYmaI2bvfGQ2tlw-8n-bxMz2KXNxPKXwumS6BEZkwVjWnkWheQiu-mjQDhD307nuQoRBNI1rTeWc46C2EUZ1bm8w9MkkEkQLrMMem9W-lzvQcHBWrmdMqSztgQGHiEy-vQMuJy78bjhY0vMMTe3ro7Ai9FG0SHKUE-21DLFveMpvTsgNQtFwoD5HMDULoNkOpDO001V_tgeTmbjK2s3zUY3ZzE6ZpWUzFu_4PBw1Ipx0FRVFkwdL2NgSg1Q0lmX5bRTNy86idH4px-D2Ax4Fn4mQyBXXzeBw');
    };
    LoginPage.prototype.checkToken = function () {
        var token = this.createToken('R15815');
        console.log("TOKEN", token);
    };
    LoginPage.prototype.register = function () {
        this.navCtrl.push(__WEBPACK_IMPORTED_MODULE_6__register_register__["a" /* RegisterPage */]);
    };
    LoginPage = LoginPage_1 = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_1__angular_core__["m" /* Component */])({
            selector: 'page-login',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/login/login.html"*/'<!--\n  Generated template for the LoginPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n    <ion-navbar class = "loginHeader">\n    <ion-title>Login</ion-title>\n    </ion-navbar>\n  \n\n</ion-header>\n\n\n<ion-content padding>\n<img src="assets/imgs/finallogo.png" class = "center">\n<ion-item>\n<ion-label floating>Email Address</ion-label>\n<ion-input type="text" [(ngModel)]="user.email"></ion-input>\n</ion-item>\n<div class = "password_field">\n<ion-item>\n<ion-label floating>Password</ion-label>\n<ion-input type="password" [(ngModel)]="user.password"></ion-input>\n</ion-item>\n</div>\n<div class = "Login-Register-Button">\n<button name = "LoginButton" ion-button (click)="login(user)" >Login</button>\n<button  ion-button color="light" (click)="register()">Register</button>\n<button ion-button (click) = "linkedInLogin()" >linkedin</button>\n<a href = "https://www.linkedin.com/oauth/v2/authorization?format=json&response_type=code&client_id=7818gxiruyce0r&redirect_uri=http://localhost/callback&state=Listenuptesting&r_basicprofile%20r_emailaddress">HI</a>\n</div>\n<button ion-button (click) = "createToken()" >token</button>\n<div *ngIf = "testingBool"> {{testingInfo}} TEST</div>\n<button ion-button (click) = "testingBool = true"></button>\n\n\n<button ion-button (click) = "linkedLogin()">Native Linkedin</button>\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/login/login.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_3_angularfire2_auth__["a" /* AngularFireAuth */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["m" /* Platform */],
            __WEBPACK_IMPORTED_MODULE_5__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["i" /* MenuController */],
            __WEBPACK_IMPORTED_MODULE_7__ionic_native_linkedin__["a" /* LinkedIn */],
            __WEBPACK_IMPORTED_MODULE_0__angular_http__["b" /* Http */],
            __WEBPACK_IMPORTED_MODULE_9__ionic_native_in_app_browser__["a" /* InAppBrowser */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["h" /* LoadingController */],
            __WEBPACK_IMPORTED_MODULE_11__ionic_native_http__["a" /* HTTP */],
            __WEBPACK_IMPORTED_MODULE_2_ionic_angular__["b" /* AlertController */],
            __WEBPACK_IMPORTED_MODULE_10__angular_common_http__["a" /* HttpClient */]])
    ], LoginPage);
    return LoginPage;
    var LoginPage_1;
}());

//# sourceMappingURL=login.js.map

/***/ }),

/***/ 66:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return CreateuserPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__tabs_tabs__ = __webpack_require__(59);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__ = __webpack_require__(28);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5_angularfire2_auth__ = __webpack_require__(29);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_firebase__ = __webpack_require__(64);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_firebase___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_6_firebase__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};







var CreateuserPage = /** @class */ (function () {
    function CreateuserPage(navCtrl, navParams, uInfo, afData, afAuth) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.uInfo = uInfo;
        this.afData = afData;
        this.afAuth = afAuth;
        this.rootPage = CreateuserPage_1;
        this.user = {
            username: "",
            firstname: "",
            lastname: ""
        };
        this.regUser = /^[a-z0-9]+$/i;
        this.regName = /^[a-z]+$/i;
        // this.setNameInfo();
        this.getTempInfo();
        this.uniqueUser = false;
    }
    CreateuserPage_1 = CreateuserPage;
    //----------------------GETTING TEMPORARY VALUE OF THE USER FOR LATER ADDING IT TO THE OBJECT OF ALL THE INFORMATION OF USER---
    CreateuserPage.prototype.getTempInfo = function () {
        var _this = this;
        this.afData.database.ref("users").child(this.uInfo.getUserId()).once("value", function (datasnap) {
            _this.tempInfo = datasnap.val();
        });
    };
    CreateuserPage.prototype.finishReg = function () {
        var _this = this;
        var ref = __WEBPACK_IMPORTED_MODULE_6_firebase__["database"]().ref("usernames");
        ref.orderByChild("username").equalTo(this.user.username).once("value", function (snapshot) {
            if (snapshot.val()) {
                _this.uniqueUser = false;
                console.log("not unique username");
            }
            else {
                _this.uniqueUser = true;
                console.log("Unique username");
                var infoObj = {
                    firstname: _this.user.firstname,
                    lastname: _this.user.lastname,
                    username: _this.user.username,
                    allowAnnon: true,
                    blocked: { 'user': "id" },
                    photourl: "https://firebasestorage.googleapis.com/v0/b/eoko-cc928.appspot.com/o/profiles%2Fdefault_avatar.jpg?alt=media&token=761a4187-2508-44fb-994c-9bd0b6842181"
                };
                if (_this.checkEmpty(_this.user) && _this.uniqueUser && _this.regUser.test(_this.user.username)
                    && _this.regName.test(_this.user.firstname)
                    && _this.regName.test(_this.user.lastname)) {
                    _this.afData.database.ref('users').child(_this.tempInfo.id).update(infoObj).then(function (winning) {
                        console.log("all is done");
                        return;
                    });
                    //------------ADD THIS USERNAME TO THE LIST OF USERNAMES FOR CHECKING UNIQUE USERNAMES LATER
                    var obj = {};
                    obj["username"] = _this.user.username;
                    _this.afData.database.ref('usernames').child(_this.tempInfo.id).update(obj);
                    _this.uInfo.setUserInfoById(_this.tempInfo.id);
                    _this.loadUserInfo();
                }
                else {
                    console.log("something happend! fix itttttt");
                    return;
                }
                '';
            }
        });
    };
    CreateuserPage.prototype.checkEmpty = function (user) {
        for (var i in user) {
            console.log(user[i]);
            if (user[i] == '' || user[i] == " " || !(user[i])) {
                return false;
            }
        }
        return true;
    };
    CreateuserPage.prototype.loadUserInfo = function () {
        var _this = this;
        this.usrInfo = this.uInfo.getUserInfo();
        var length = Object.keys(this.usrInfo).length;
        console.log("length", length);
        if (length == 2) {
            setTimeout(function () {
                _this.loadUserInfo();
            }, 1000);
        }
        else {
            this.navCtrl.setRoot(__WEBPACK_IMPORTED_MODULE_2__tabs_tabs__["a" /* TabsPage */]);
        }
    };
    CreateuserPage = CreateuserPage_1 = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-createuser',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/createuser/createuser.html"*/'<!--\n  Generated template for the CreateuserPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n\n  <ion-navbar>\n    <ion-title>createuser</ion-title>\n  </ion-navbar>\n\n</ion-header>\n\n\n<ion-content padding>\n\n  <ion-item>\n  <ion-label floating> User Name</ion-label>\n  <ion-input type = "text" [(ngModel)] = "user.username"></ion-input>\n  </ion-item>\n\n  <ion-item>\n  <ion-label floating> First Name</ion-label>\n  <ion-input type = "text" [(ngModel)] = "user.firstname"></ion-input>\n  </ion-item>\n\n  <ion-item>\n  <ion-label floating> Last Name</ion-label>\n  <ion-input type = "text" [(ngModel)] = "user.lastname"></ion-input>\n  </ion-item>\n  <button id = "RegisterButton" ion-button (click)="finishReg()">Finish your setup!</button>\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/createuser/createuser.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */],
            __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */],
            __WEBPACK_IMPORTED_MODULE_3__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */],
            __WEBPACK_IMPORTED_MODULE_5_angularfire2_auth__["a" /* AngularFireAuth */]])
    ], CreateuserPage);
    return CreateuserPage;
    var CreateuserPage_1;
}());

//# sourceMappingURL=createuser.js.map

/***/ })

},[255]);
//# sourceMappingURL=main.js.map
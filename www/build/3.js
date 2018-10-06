webpackJsonp([3],{

/***/ 402:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SearchuserPageModule", function() { return SearchuserPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__searchuser__ = __webpack_require__(414);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var SearchuserPageModule = /** @class */ (function () {
    function SearchuserPageModule() {
    }
    SearchuserPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__searchuser__["a" /* SearchuserPage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__searchuser__["a" /* SearchuserPage */]),
            ],
            exports: [
                __WEBPACK_IMPORTED_MODULE_2__searchuser__["a" /* SearchuserPage */]
            ],
            entryComponents: [
                __WEBPACK_IMPORTED_MODULE_2__searchuser__["a" /* SearchuserPage */]
            ]
        })
    ], SearchuserPageModule);
    return SearchuserPageModule;
}());

//# sourceMappingURL=searchuser.module.js.map

/***/ }),

/***/ 414:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return SearchuserPage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__ = __webpack_require__(23);
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




// import{SendfeedPage} from '../sendfeed/sendfeed';
/**
 * Generated class for the SearchuserPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */
var SearchuserPage = /** @class */ (function () {
    function SearchuserPage(navCtrl, navParams, uInfo) {
        this.navCtrl = navCtrl;
        this.navParams = navParams;
        this.uInfo = uInfo;
        this.i = 0;
        var usrId = this.uInfo.getUserInfo().id;
        this.usrData = this.uInfo.getUserInfo();
        this.userList = this.uInfo.getUserNames();
        this.objKeys = Object.keys(this.userList);
        this.blockKeys = Object.keys(this.usrData.blocked);
        this.getPhotos();
        console.log("usernames", this.userList);
        this.usersArray = [];
        this.indivUsernames = [];
        for (var i in this.objKeys) {
            for (var j in this.blockKeys) {
                if (this.objKeys[i] == this.blockKeys[j] || this.objKeys[i] == this.usrData.id) {
                    delete this.userList[this.objKeys[i]];
                }
            }
        }
        for (var k in this.userList) {
            var obj = {};
            obj[k] = this.userList[k].username;
            this.usersArray.push(obj);
            this.indivUsernames.push({ "username": this.userList[k].username,
                "id": k });
        }
        console.log("array of users", this.usersArray);
        console.log("indiv usernames", this.indivUsernames);
        this.userList = [];
    }
    //------------SEARCHING USERS--------------------
    SearchuserPage.prototype.searchUsers = function (searchbar) {
        var _this = this;
        this.userList = this.indivUsernames;
        this.q = searchbar.srcElement.value;
        console.log('searching...', this.q);
        if (!this.q) {
            this.userList = [];
            return;
        }
        ;
        if (String(this.q).replace(/\s/g, "").length == 0) {
            this.userList = [];
            return true;
        }
        this.userList = this.userList.filter(function (v) {
            if (v.username && _this.q) {
                if (v.username.toLowerCase().indexOf(_this.q.toLowerCase()) > -1) {
                    return true;
                }
                return false;
            }
        });
    };
    //-------------GO TO SENDFEED PAGE---------------
    SearchuserPage.prototype.goToSend = function (user) {
        this.navCtrl.push("SendfeedPage", {
            param1: user
        });
        this.usrData = user;
    };
    SearchuserPage.prototype.getPhotos = function () {
        return __awaiter(this, void 0, void 0, function () {
            var _this = this;
            var _a, _b, _i, i, j;
            return __generator(this, function (_c) {
                switch (_c.label) {
                    case 0:
                        this.userPhoto = [];
                        _a = [];
                        for (_b in this.objKeys)
                            _a.push(_b);
                        _i = 0;
                        _c.label = 1;
                    case 1:
                        if (!(_i < _a.length)) return [3 /*break*/, 4];
                        i = _a[_i];
                        return [4 /*yield*/, __WEBPACK_IMPORTED_MODULE_3_firebase__["storage"]().ref('profiles').child(this.objKeys[i] + ".jpg").getDownloadURL().then(function (success) {
                                _this.userPhoto[_this.objKeys[i]] = success;
                            }, function (fail) {
                                _this.userPhoto[_this.objKeys[i]] = 'http://debut.careers/wp-content/uploads/2017/04/Profile-Fallback-01-01.png?x28372';
                            })];
                    case 2:
                        _c.sent();
                        _c.label = 3;
                    case 3:
                        _i++;
                        return [3 /*break*/, 1];
                    case 4:
                        for (j in this.indivUsernames) {
                            this.indivUsernames[j].photourl = this.userPhoto[this.indivUsernames[j].id];
                        }
                        return [2 /*return*/];
                }
            });
        });
    };
    SearchuserPage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-searchuser',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/searchuser/searchuser.html"*/'<!--\n  Generated template for the SearchuserPage page.\n\n  See http://ionicframework.com/docs/components/#navigation for more info on\n  Ionic pages and navigation.\n-->\n<ion-header>\n  <ion-navbar color = "primary">\n\n  	<!-- <ion-toolbar color = "white"> -->\n  	<ion-title>\n		<ion-searchbar autocomplete autocorrect placeholder = "Enter username to search" (ionInput) = "searchUsers($event)" ></ion-searchbar>\n	<!-- </ion-toolbar> -->\n	</ion-title>\n\n  </ion-navbar>\n\n</ion-header>\n\n<ion-content>\n	<h5 id = "A3"></h5>\n	<ion-list>\n		<ion-item ion-item *ngFor = "let user of userList" (click) = "goToSend(user)">\n			 <img [src] = "user.photourl"> <!-- <h3 id = "A1">{{user.firstname}} {{user.lastname}}</h3> --><p id = "A2">@{{user.username}}</p>\n		</ion-item>\n	</ion-list>\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/searchuser/searchuser.html"*/,
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */], __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["l" /* NavParams */], __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__["a" /* UserInfoProvider */]])
    ], SearchuserPage);
    return SearchuserPage;
}());

//# sourceMappingURL=searchuser.js.map

/***/ })

});
//# sourceMappingURL=3.js.map
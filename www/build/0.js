webpackJsonp([0],{

/***/ 399:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MessagePageModule", function() { return MessagePageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__message__ = __webpack_require__(408);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



// import { IonicImageLoader } from 'ionic-image-loader';
var MessagePageModule = /** @class */ (function () {
    function MessagePageModule() {
    }
    MessagePageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["I" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_2__message__["a" /* MessagePage */],
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_1_ionic_angular__["g" /* IonicPageModule */].forChild(__WEBPACK_IMPORTED_MODULE_2__message__["a" /* MessagePage */]),
            ],
            exports: [
                __WEBPACK_IMPORTED_MODULE_2__message__["a" /* MessagePage */]
            ],
            entryComponents: [
                __WEBPACK_IMPORTED_MODULE_2__message__["a" /* MessagePage */]
            ]
        })
    ], MessagePageModule);
    return MessagePageModule;
}());

//# sourceMappingURL=message.module.js.map

/***/ }),

/***/ 408:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return MessagePage; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__(0);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_ionic_angular__ = __webpack_require__(10);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__ = __webpack_require__(23);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_rxjs_add_operator_take__ = __webpack_require__(409);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_rxjs_add_operator_take___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3_rxjs_add_operator_take__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__ = __webpack_require__(28);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};





//3rd party libraries
var MessagePage = /** @class */ (function () {
    function MessagePage(navCtrl
        //private chatInfo: ChatInfoProvider
        , uInfo, afData
        //,private afAuth: AngularFireAuth
    ) {
        this.navCtrl = navCtrl;
        this.uInfo = uInfo;
        this.afData = afData;
        this.chatArray = [];
        //Initialize variables
        this.usrId = this.uInfo.getUserInfo().id;
        //Call functions here
        this.loadDMs();
    }
    MessagePage.prototype.loadDMs = function () {
        var _this = this;
        this.chatList$ = this.afData.list("users/" + this.usrId + "/chats/DMs").snapshotChanges();
        this.chatListSubscription = this.chatList$.subscribe(function (chatArr) {
            _this.chatArray = chatArr;
            _this.chatArray.forEach(function (chat) {
                var otherID = chat.key;
                _this.uInfo.getOtherUserInfo(otherID).take(1).subscribe(function (otherInfo) {
                    chat.otherInfo = otherInfo;
                });
            });
            console.log("cahts are here", _this.chatArray);
            _this.constArray = _this.chatArray;
        });
    };
    MessagePage.prototype.deleteChat = function (chat) {
        var position = null;
        this.afData.database.ref('users').child(this.usrId).child('chats').child('DMs').child(chat.key).remove();
        for (var i in this.chatArray) {
            if (this.chatArray[i].key == chat.key) {
                position = i;
            }
        }
        this.chatArray.splice(position, 1);
    };
    MessagePage.prototype.goToChatDetail = function (chatID, otherID) {
        this.navCtrl.push("MessageDetailPage", { chatID: chatID, otherID: otherID });
    };
    MessagePage.prototype.searchMessage = function (searchbar) {
        var _this = this;
        this.chatArray = this.constArray;
        this.q = searchbar.srcElement.value;
        console.log('searching...', this.q);
        if (!this.q) {
            return;
        }
        ;
        if (String(this.q).replace(/\s/g, "").length == 0) {
            return true;
        }
        this.chatArray = this.chatArray.filter(function (v) {
            if (v.otherInfo.username && v.otherInfo.email && _this.q) {
                if (v.otherInfo.username.toLowerCase().indexOf(_this.q.toLowerCase()) > -1 ||
                    v.otherInfo.email.toLowerCase().indexOf(_this.q.toLowerCase()) > -1) {
                    return true;
                }
                return false;
            }
        });
    };
    MessagePage.prototype.ionViewDidLeave = function () {
    };
    MessagePage = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'page-message',template:/*ion-inline-start:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/message/message.html"*/'<ion-header>\n  <ion-navbar color="primary"> \n   <!--  <ion-buttons>\n      <button ion-button icon-only menuToggle class = "menu-button" side="left" class = "menu-button">\n        Listen Up\n      </button>\n    </ion-buttons> -->\n  <ion-toolbar color = "white">\n  <ion-searchbar autocomplete autocorrect placeholder = "Search messages, enter either email or username" (ionInput) = "searchMessage($event)"></ion-searchbar>\n  </ion-toolbar>\n  </ion-navbar>\n</ion-header>\n\n<ion-content padding>\n  <ion-list class = "chat-list">\n    <ng-container *ngFor="let chat of chatArray">\n       <ion-item-sliding>\n        <ion-item  (click)="goToChatDetail(chat.payload.val().chatID, chat.otherInfo.id)">\n          <ion-avatar item-start><ion-img src="{{chat.otherInfo?.photourl}}"></ion-img></ion-avatar>\n          <h2>{{chat.otherInfo?.firstname}} {{chat.otherInfo?.lastname}}</h2>\n          <p>{{chat.payload.val().lastText}}</p>\n          <p item-right>{{chat.payload.val().timestamp | date:\'EEE hh:mm a\'}}</p>\n          </ion-item>\n          <ion-item-options>\n                <button ion-button (click) = "deleteChat(chat)">delete</button>\n          </ion-item-options>\n          </ion-item-sliding>\n    </ng-container>\n  </ion-list>\n</ion-content>\n'/*ion-inline-end:"/Users/wanghui/Desktop/Feedback/feedbackID/src/pages/message/message.html"*/
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1_ionic_angular__["k" /* NavController */]
            //private chatInfo: ChatInfoProvider
            ,
            __WEBPACK_IMPORTED_MODULE_2__providers_userInfo_userInfo__["a" /* UserInfoProvider */],
            __WEBPACK_IMPORTED_MODULE_4_angularfire2_database__["a" /* AngularFireDatabase */]
            //,private afAuth: AngularFireAuth
        ])
    ], MessagePage);
    return MessagePage;
}());

//# sourceMappingURL=message.js.map

/***/ }),

/***/ 409:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var Observable_1 = __webpack_require__(3);
var take_1 = __webpack_require__(410);
Observable_1.Observable.prototype.take = take_1.take;
//# sourceMappingURL=take.js.map

/***/ }),

/***/ 410:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var take_1 = __webpack_require__(411);
/**
 * Emits only the first `count` values emitted by the source Observable.
 *
 * <span class="informal">Takes the first `count` values from the source, then
 * completes.</span>
 *
 * <img src="./img/take.png" width="100%">
 *
 * `take` returns an Observable that emits only the first `count` values emitted
 * by the source Observable. If the source emits fewer than `count` values then
 * all of its values are emitted. After that, it completes, regardless if the
 * source completes.
 *
 * @example <caption>Take the first 5 seconds of an infinite 1-second interval Observable</caption>
 * var interval = Rx.Observable.interval(1000);
 * var five = interval.take(5);
 * five.subscribe(x => console.log(x));
 *
 * @see {@link takeLast}
 * @see {@link takeUntil}
 * @see {@link takeWhile}
 * @see {@link skip}
 *
 * @throws {ArgumentOutOfRangeError} When using `take(i)`, it delivers an
 * ArgumentOutOrRangeError to the Observer's `error` callback if `i < 0`.
 *
 * @param {number} count The maximum number of `next` values to emit.
 * @return {Observable<T>} An Observable that emits only the first `count`
 * values emitted by the source Observable, or all of the values from the source
 * if the source emits fewer than `count` values.
 * @method take
 * @owner Observable
 */
function take(count) {
    return take_1.take(count)(this);
}
exports.take = take;
//# sourceMappingURL=take.js.map

/***/ }),

/***/ 411:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Subscriber_1 = __webpack_require__(13);
var ArgumentOutOfRangeError_1 = __webpack_require__(412);
var EmptyObservable_1 = __webpack_require__(122);
/**
 * Emits only the first `count` values emitted by the source Observable.
 *
 * <span class="informal">Takes the first `count` values from the source, then
 * completes.</span>
 *
 * <img src="./img/take.png" width="100%">
 *
 * `take` returns an Observable that emits only the first `count` values emitted
 * by the source Observable. If the source emits fewer than `count` values then
 * all of its values are emitted. After that, it completes, regardless if the
 * source completes.
 *
 * @example <caption>Take the first 5 seconds of an infinite 1-second interval Observable</caption>
 * var interval = Rx.Observable.interval(1000);
 * var five = interval.take(5);
 * five.subscribe(x => console.log(x));
 *
 * @see {@link takeLast}
 * @see {@link takeUntil}
 * @see {@link takeWhile}
 * @see {@link skip}
 *
 * @throws {ArgumentOutOfRangeError} When using `take(i)`, it delivers an
 * ArgumentOutOrRangeError to the Observer's `error` callback if `i < 0`.
 *
 * @param {number} count The maximum number of `next` values to emit.
 * @return {Observable<T>} An Observable that emits only the first `count`
 * values emitted by the source Observable, or all of the values from the source
 * if the source emits fewer than `count` values.
 * @method take
 * @owner Observable
 */
function take(count) {
    return function (source) {
        if (count === 0) {
            return new EmptyObservable_1.EmptyObservable();
        }
        else {
            return source.lift(new TakeOperator(count));
        }
    };
}
exports.take = take;
var TakeOperator = (function () {
    function TakeOperator(total) {
        this.total = total;
        if (this.total < 0) {
            throw new ArgumentOutOfRangeError_1.ArgumentOutOfRangeError;
        }
    }
    TakeOperator.prototype.call = function (subscriber, source) {
        return source.subscribe(new TakeSubscriber(subscriber, this.total));
    };
    return TakeOperator;
}());
/**
 * We need this JSDoc comment for affecting ESDoc.
 * @ignore
 * @extends {Ignored}
 */
var TakeSubscriber = (function (_super) {
    __extends(TakeSubscriber, _super);
    function TakeSubscriber(destination, total) {
        _super.call(this, destination);
        this.total = total;
        this.count = 0;
    }
    TakeSubscriber.prototype._next = function (value) {
        var total = this.total;
        var count = ++this.count;
        if (count <= total) {
            this.destination.next(value);
            if (count === total) {
                this.destination.complete();
                this.unsubscribe();
            }
        }
    };
    return TakeSubscriber;
}(Subscriber_1.Subscriber));
//# sourceMappingURL=take.js.map

/***/ }),

/***/ 412:
/***/ (function(module, exports, __webpack_require__) {

"use strict";

var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * An error thrown when an element was queried at a certain index of an
 * Observable, but no such index or position exists in that sequence.
 *
 * @see {@link elementAt}
 * @see {@link take}
 * @see {@link takeLast}
 *
 * @class ArgumentOutOfRangeError
 */
var ArgumentOutOfRangeError = (function (_super) {
    __extends(ArgumentOutOfRangeError, _super);
    function ArgumentOutOfRangeError() {
        var err = _super.call(this, 'argument out of range');
        this.name = err.name = 'ArgumentOutOfRangeError';
        this.stack = err.stack;
        this.message = err.message;
    }
    return ArgumentOutOfRangeError;
}(Error));
exports.ArgumentOutOfRangeError = ArgumentOutOfRangeError;
//# sourceMappingURL=ArgumentOutOfRangeError.js.map

/***/ })

});
//# sourceMappingURL=0.js.map
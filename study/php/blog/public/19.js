webpackJsonp([19],{

/***/ 188:
/***/ (function(module, exports, __webpack_require__) {

var disposed = false
function injectStyle (ssrContext) {
  if (disposed) return
  __webpack_require__(400)
}
var normalizeComponent = __webpack_require__(1)
/* script */
var __vue_script__ = __webpack_require__(402)
/* template */
var __vue_template__ = __webpack_require__(403)
/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = injectStyle
/* scopeId */
var __vue_scopeId__ = "data-v-eb55ec6c"
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __vue_script__,
  __vue_template__,
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)
Component.options.__file = "resources/assets/js/dashboard/modules/file/File.vue"

/* hot reload */
if (false) {(function () {
  var hotAPI = require("vue-hot-reload-api")
  hotAPI.install(require("vue"), false)
  if (!hotAPI.compatible) return
  module.hot.accept()
  if (!module.hot.data) {
    hotAPI.createRecord("data-v-eb55ec6c", Component.options)
  } else {
    hotAPI.reload("data-v-eb55ec6c", Component.options)
  }
  module.hot.dispose(function (data) {
    disposed = true
  })
})()}

module.exports = Component.exports


/***/ }),

/***/ 400:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(401);
if(typeof content === 'string') content = [[module.i, content, '']];
if(content.locals) module.exports = content.locals;
// add the styles to the DOM
var update = __webpack_require__(4)("334336b8", content, false, {});
// Hot Module Replacement
if(false) {
 // When the styles change, update the <style> tags
 if(!content.locals) {
   module.hot.accept("!!../../../../../../node_modules/css-loader/index.js!../../../../../../node_modules/vue-loader/lib/style-compiler/index.js?{\"vue\":true,\"id\":\"data-v-eb55ec6c\",\"scoped\":true,\"hasInlineConfig\":true}!../../../../../../node_modules/sass-loader/lib/loader.js!../../../../../../node_modules/vue-loader/lib/selector.js?type=styles&index=0!./File.vue", function() {
     var newContent = require("!!../../../../../../node_modules/css-loader/index.js!../../../../../../node_modules/vue-loader/lib/style-compiler/index.js?{\"vue\":true,\"id\":\"data-v-eb55ec6c\",\"scoped\":true,\"hasInlineConfig\":true}!../../../../../../node_modules/sass-loader/lib/loader.js!../../../../../../node_modules/vue-loader/lib/selector.js?type=styles&index=0!./File.vue");
     if(typeof newContent === 'string') newContent = [[module.id, newContent, '']];
     update(newContent);
   });
 }
 // When the module is disposed, remove the <style> tags
 module.hot.dispose(function() { update(); });
}

/***/ }),

/***/ 401:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(2)(false);
// imports


// module
exports.push([module.i, "\n.box-content .btn[data-v-eb55ec6c] {\n  display: inline-block;\n  border-radius: 50%;\n  width: 2.2rem;\n  height: 2.2rem;\n  line-height: 2.2rem;\n  padding: 0;\n  margin-left: 5px;\n  margin-right: 5px;\n}\nh5[data-v-eb55ec6c] {\n  margin-bottom: 0;\n  font-weight: 400;\n}\n.breadcrumb[data-v-eb55ec6c] {\n  padding: 0.25rem .7rem !important;\n  margin: 0;\n}\n.box-body button[data-v-eb55ec6c],\n.box-body button[data-v-eb55ec6c]:hover {\n  padding: 0;\n  border-radius: 50%;\n  width: 2.5em;\n  height: 2.5em;\n  outline: none;\n}\n.preview-size[data-v-eb55ec6c] {\n  width: 100%;\n}\n.file-upload input[data-v-eb55ec6c] {\n  width: 71px;\n  cursor: pointer;\n  position: absolute;\n  top: 0;\n  opacity: 0;\n}\n", ""]);

// exports


/***/ }),

/***/ 402:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _Modal = __webpack_require__(26);

var _Modal2 = _interopRequireDefault(_Modal);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

exports.default = {
  components: {
    Modal: _Modal2.default
  },
  data: function data() {
    return {
      folder: '',
      files: null,
      file_name: '',
      path: '',
      upload: {},
      showFolder: false,
      showFile: false,
      showImage: false,
      preview_image: '',
      fields: [{
        name: 'name',
        title: 'ID',
        titleClass: 'text-center',
        dataClass: 'text-center'
      }, {
        name: 'user',
        title: 'User Name',
        titleClass: 'text-center',
        dataClass: 'text-center',
        callback: 'username'
      }, {
        name: 'title',
        title: 'Title'
      }, {
        name: "content",
        title: 'Content',
        callback: 'content'
      }, {
        name: 'status',
        title: 'Status',
        titleClass: 'text-center',
        dataClass: 'text-center',
        callback: 'status'
      }, {
        name: 'created_at',
        title: 'Created At'
      }, {
        name: '__actions',
        dataClass: 'text-center'
      }]
    };
  },
  mounted: function mounted() {
    this.getFileInfo(this.$route.query.folder);
  },

  methods: {
    preview: function preview(path) {
      this.showImage = true;
      this.preview_image = path;
    },
    confirm: function confirm() {
      var _this = this;

      if (!this.folder) {
        toastr.error('The folder name must be required!');
        return;
      }

      var path = this.upload.folder == '/' ? '' : this.upload.folder;

      this.path = path + '/' + this.folder;

      this.$http.post('folder', { folder: this.path }).then(function (response) {
        toastr.success('You create a new folder success!');

        _this.showFolder = false;
        _this.$set(_this.upload.subfolders, _this.path, _this.folder);
        _this.folder = '';
      }).catch(function (_ref) {
        var response = _ref.response;

        toastr.error(response.status + ' : ' + response.statusText);
      });
    },
    change: function change(event) {
      this.files = event.target.files;
    },
    uploadFile: function uploadFile() {
      var _this2 = this;

      if (!this.files) {
        toastr.error('The file must be required');
        return;
      }

      var formData = new FormData();

      formData.append('file', this.files[0]);
      formData.append('name', this.file_name);
      formData.append('folder', this.upload.folder);

      this.$http.post('upload', formData).then(function (response) {
        toastr.success('You upload a file success!');

        var file = {
          fullPath: response.data.real_path,
          mimeType: response.data.mime,
          name: response.data.original_name,
          size: response.data.size,
          webPath: response.data.url
        };

        _this2.upload.files.push(file);
        _this2.file_name = '';
        _this2.showFile = false;
      }).catch(function (_ref2) {
        var response = _ref2.response;

        if (response.data.error) {
          toastr.error(response.data.error.message);
        } else {
          toastr.error(response.status + ' : Resource ' + response.statusText);
        }
      });
    },
    deleteFolder: function deleteFolder(name) {
      var _this3 = this;

      var path = this.upload.folder == '/' ? '' : this.upload.folder;
      this.$http.post('folder/delete', { del_folder: name, folder: this.upload.folder }).then(function (response) {
        toastr.success('You delete a folder success!');

        _this3.$delete(_this3.upload.subfolders, path + '/' + name);
      }).catch(function (_ref3) {
        var response = _ref3.response;

        if (response.data.error) {
          toastr.error(response.data.error.http_code + ' : Resource ' + response.data.error.message);
        } else {
          toastr.error(response.status + ' : Resource ' + response.statusText);
        }
      });
    },
    deleteFile: function deleteFile(file, index) {
      var _this4 = this;

      this.$http.post('file/delete', { path: file.fullPath }).then(function (response) {
        toastr.success('You delete a file success!');

        _this4.upload.files.splice(index, 1);
      }).catch(function (_ref4) {
        var response = _ref4.response;

        toastr.error(response.status + ' : Resource ' + response.statusText);
      });
    },
    getFileInfo: function getFileInfo(path) {
      var _this5 = this;

      var url = 'upload';

      if (path) {
        url = url + '?folder=' + path;
      } else {
        path = '/';
      }

      this.$http.get(url).then(function (response) {
        _this5.upload = response.data.data;
        if (_this5.upload.subfolders instanceof Array) {
          _this5.upload.subfolders = {};
        }
        _this5.$router.push({ name: 'dashboard.file', query: { folder: path } });
      });
    },
    checkImageType: function checkImageType(fileType) {
      if (fileType != null) {
        return fileType.indexOf("image/") != -1;
      }

      return false;
    }
  }
}; //
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/***/ }),

/***/ 403:
/***/ (function(module, exports, __webpack_require__) {

var render = function() {
  var _vm = this
  var _h = _vm.$createElement
  var _c = _vm._self._c || _h
  return _c(
    "div",
    { staticClass: "row" },
    [
      _c("div", { staticClass: "box" }, [
        _c("div", { staticClass: "box-title" }, [
          _c("div", { staticClass: "row d-flex m-0" }, [
            _c(
              "div",
              { staticClass: "col-md-6 d-flex align-items-center p-0" },
              [
                _c("h5", { staticClass: "align-self-center" }, [
                  _vm._v(_vm._s(_vm.$t("page.files")) + "  ")
                ]),
                _vm._v(" "),
                _c("div", { staticClass: "float-left" }, [
                  _c("nav", { attrs: { "aria-label": "breadcrumb" } }, [
                    _c(
                      "ol",
                      { staticClass: "breadcrumb" },
                      [
                        _vm._l(_vm.upload.breadcrumbs, function(disp, path) {
                          return _c("li", { staticClass: "breadcrumb-item" }, [
                            _c(
                              "a",
                              {
                                attrs: { href: "javascript:;" },
                                on: {
                                  click: function($event) {
                                    _vm.getFileInfo(path)
                                  }
                                }
                              },
                              [
                                _vm._v(
                                  "\n                    " +
                                    _vm._s(disp) +
                                    "\n                  "
                                )
                              ]
                            )
                          ])
                        }),
                        _vm._v(" "),
                        _c("li", { staticClass: "breadcrumb-item active" }, [
                          _vm._v(_vm._s(_vm.upload.folderName))
                        ])
                      ],
                      2
                    )
                  ])
                ])
              ]
            ),
            _vm._v(" "),
            _c(
              "div",
              { staticClass: "col-md-6 align-items-center p-0 text-right" },
              [
                _c("small", [
                  _vm.checkPermission("CREATE_FILE_FOLDER")
                    ? _c(
                        "button",
                        {
                          staticClass: "btn btn-success btn-sm",
                          attrs: { type: "button" },
                          on: {
                            click: function($event) {
                              _vm.showFolder = true
                            }
                          }
                        },
                        [
                          _c("i", { staticClass: "fas fa-plus-circle" }),
                          _vm._v(
                            " " +
                              _vm._s(_vm.$t("table.new_folder")) +
                              "\n            "
                          )
                        ]
                      )
                    : _vm._e(),
                  _vm._v(" "),
                  _vm.checkPermission("UPLOAD_FILE")
                    ? _c(
                        "button",
                        {
                          staticClass: "btn btn-primary btn-sm",
                          attrs: { type: "button" },
                          on: {
                            click: function($event) {
                              _vm.showFile = true
                            }
                          }
                        },
                        [
                          _c("i", { staticClass: "fas fa-inbox" }),
                          _vm._v(
                            " " +
                              _vm._s(_vm.$t("table.upload")) +
                              "\n            "
                          )
                        ]
                      )
                    : _vm._e()
                ])
              ]
            )
          ])
        ]),
        _vm._v(" "),
        _c("div", { staticClass: "box-content p-0" }, [
          _c(
            "table",
            {
              staticClass: "table table-striped table-hover",
              attrs: { id: "uploads-table" }
            },
            [
              _c(
                "tbody",
                [
                  _c("tr", [
                    _c("th", [_vm._v(_vm._s(_vm.$t("table.name")))]),
                    _vm._v(" "),
                    _c("th", [_vm._v(_vm._s(_vm.$t("table.type")))]),
                    _vm._v(" "),
                    _c("th", [_vm._v(_vm._s(_vm.$t("table.date")))]),
                    _vm._v(" "),
                    _c("th", [_vm._v(_vm._s(_vm.$t("table.size")))]),
                    _vm._v(" "),
                    _c("th", [_vm._v(_vm._s(_vm.$t("table.action")))])
                  ]),
                  _vm._v(" "),
                  _vm._l(_vm.upload.subfolders, function(name, path) {
                    return _c("tr", [
                      _c("td", [
                        _c(
                          "a",
                          {
                            attrs: { href: "javascript:;" },
                            on: {
                              click: function($event) {
                                _vm.getFileInfo(path)
                              }
                            }
                          },
                          [
                            _c("i", { staticClass: "fas fa-folder" }),
                            _vm._v(
                              "\n                " +
                                _vm._s(name) +
                                "\n              "
                            )
                          ]
                        )
                      ]),
                      _vm._v(" "),
                      _c("td", [_vm._v("-")]),
                      _vm._v(" "),
                      _c("td", [_vm._v("-")]),
                      _vm._v(" "),
                      _c("td", [_vm._v("-")]),
                      _vm._v(" "),
                      _c("td", [
                        _c(
                          "a",
                          {
                            staticClass: "btn btn-sm btn-secondary",
                            attrs: { href: "javascript:;" },
                            on: {
                              click: function($event) {
                                _vm.getFileInfo(path)
                              }
                            }
                          },
                          [_c("i", { staticClass: "fas fa-folder-open" })]
                        ),
                        _vm._v(" "),
                        _vm.checkPermission("DESTROY_FILE")
                          ? _c(
                              "button",
                              {
                                staticClass: "btn btn-sm btn-danger",
                                attrs: { type: "button" },
                                on: {
                                  click: function($event) {
                                    _vm.deleteFolder(name)
                                  }
                                }
                              },
                              [_c("i", { staticClass: "fas fa-trash-alt" })]
                            )
                          : _vm._e()
                      ])
                    ])
                  }),
                  _vm._v(" "),
                  _vm._l(_vm.upload.files, function(file, index) {
                    return _c(
                      "tr",
                      [
                        file.type == "folder"
                          ? [
                              _c("td", [
                                _c(
                                  "a",
                                  {
                                    attrs: { href: "javascript:;" },
                                    on: {
                                      click: function($event) {
                                        _vm.getFileInfo(file.fullPath)
                                      }
                                    }
                                  },
                                  [
                                    _c("i", { staticClass: "fas fa-folder" }),
                                    _vm._v(
                                      "\n                  " +
                                        _vm._s(file.name) +
                                        "\n                "
                                    )
                                  ]
                                )
                              ]),
                              _vm._v(" "),
                              _c("td", [_vm._v("-")]),
                              _vm._v(" "),
                              _c("td", [_vm._v("-")]),
                              _vm._v(" "),
                              _c("td", [_vm._v("-")]),
                              _vm._v(" "),
                              _c("td", [
                                _c(
                                  "a",
                                  {
                                    staticClass: "btn btn-sm btn-secondary",
                                    attrs: { href: "javascript:;" },
                                    on: {
                                      click: function($event) {
                                        _vm.getFileInfo(file.fullPath)
                                      }
                                    }
                                  },
                                  [
                                    _c("i", {
                                      staticClass: "fas fa-folder-open"
                                    })
                                  ]
                                ),
                                _vm._v(" "),
                                _vm.checkPermission("DESTROY_FILE")
                                  ? _c(
                                      "button",
                                      {
                                        staticClass: "btn btn-sm btn-danger",
                                        attrs: { type: "button" },
                                        on: {
                                          click: function($event) {
                                            _vm.deleteFolder(file.fullPath)
                                          }
                                        }
                                      },
                                      [
                                        _c("i", {
                                          staticClass: "fas fa-trash-alt"
                                        })
                                      ]
                                    )
                                  : _vm._e()
                              ])
                            ]
                          : [
                              _c("td", [
                                _c(
                                  "a",
                                  {
                                    attrs: {
                                      target: "_blank",
                                      href: file.webPath
                                    }
                                  },
                                  [
                                    _vm.checkImageType(file.mimeType)
                                      ? _c("i", { staticClass: "fas fa-image" })
                                      : _c("i", {
                                          staticClass: "fas fa-file-alt"
                                        }),
                                    _vm._v(
                                      "\n                  " +
                                        _vm._s(file.name) +
                                        "\n                "
                                    )
                                  ]
                                )
                              ]),
                              _vm._v(" "),
                              _c("td", [_vm._v(_vm._s(file.mimeType))]),
                              _vm._v(" "),
                              _c("td", [_vm._v(_vm._s(file.modified))]),
                              _vm._v(" "),
                              _c("td", [_vm._v(_vm._s(file.size))]),
                              _vm._v(" "),
                              _c("td", [
                                _vm.checkImageType(file.mimeType)
                                  ? _c(
                                      "button",
                                      {
                                        staticClass: "btn btn-sm btn-info",
                                        attrs: { type: "button" },
                                        on: {
                                          click: function($event) {
                                            _vm.preview(file.webPath)
                                          }
                                        }
                                      },
                                      [_c("i", { staticClass: "fas fa-eye" })]
                                    )
                                  : _vm._e(),
                                _vm._v(" "),
                                _vm.checkPermission("DESTROY_FILE")
                                  ? _c(
                                      "button",
                                      {
                                        staticClass: "btn btn-sm btn-danger",
                                        attrs: { type: "button" },
                                        on: {
                                          click: function($event) {
                                            _vm.deleteFile(file, index)
                                          }
                                        }
                                      },
                                      [
                                        _c("i", {
                                          staticClass: "fas fa-trash-alt"
                                        })
                                      ]
                                    )
                                  : _vm._e()
                              ])
                            ]
                      ],
                      2
                    )
                  })
                ],
                2
              )
            ]
          )
        ])
      ]),
      _vm._v(" "),
      _c(
        "modal",
        {
          attrs: { show: _vm.showFolder, "show-footer": "" },
          on: {
            confirm: _vm.confirm,
            cancel: function($event) {
              _vm.showFolder = false
            }
          }
        },
        [
          _c("template", { slot: "title" }, [
            _vm._v(_vm._s(_vm.$t("form.create_folder")))
          ]),
          _vm._v(" "),
          _c("form", [
            _c("div", { staticClass: "form-group row" }, [
              _c(
                "label",
                {
                  staticClass: "col-form-label col-sm-3",
                  attrs: { for: "folder" }
                },
                [_vm._v(_vm._s(_vm.$t("form.folder_name")))]
              ),
              _vm._v(" "),
              _c("div", { staticClass: "col-sm-8" }, [
                _c("input", {
                  directives: [
                    {
                      name: "model",
                      rawName: "v-model",
                      value: _vm.folder,
                      expression: "folder"
                    }
                  ],
                  staticClass: "form-control",
                  attrs: {
                    type: "text",
                    id: "folder",
                    placeholder: _vm.$t("form.folder_name")
                  },
                  domProps: { value: _vm.folder },
                  on: {
                    input: function($event) {
                      if ($event.target.composing) {
                        return
                      }
                      _vm.folder = $event.target.value
                    }
                  }
                })
              ])
            ])
          ])
        ],
        2
      ),
      _vm._v(" "),
      _c(
        "modal",
        {
          attrs: { show: _vm.showFile, "show-footer": "" },
          on: {
            confirm: _vm.uploadFile,
            cancel: function($event) {
              _vm.showFile = false
            }
          }
        },
        [
          _c("template", { slot: "title" }, [
            _vm._v(_vm._s(_vm.$t("form.upload_file")))
          ]),
          _vm._v(" "),
          _c("form", { attrs: { enctype: "multipart/form-data" } }, [
            _c("div", { staticClass: "form-group row" }, [
              _c(
                "label",
                {
                  staticClass: "col-form-label col-sm-3",
                  attrs: { for: "file" }
                },
                [_vm._v(_vm._s(_vm.$t("form.file")))]
              ),
              _vm._v(" "),
              _c("div", { staticClass: "col-sm-8 file-upload" }, [
                _c(
                  "button",
                  { staticClass: "btn btn-primary", attrs: { type: "button" } },
                  [_vm._v(_vm._s(_vm.$t("table.upload")))]
                ),
                _vm._v(" "),
                _c("input", {
                  staticClass: "form-control",
                  attrs: { type: "file", id: "file", name: "file" },
                  on: { change: _vm.change }
                })
              ])
            ]),
            _vm._v(" "),
            _c("div", { staticClass: "form-group row" }, [
              _c(
                "label",
                {
                  staticClass: "col-form-label col-sm-3",
                  attrs: { for: "file_name" }
                },
                [_vm._v(_vm._s(_vm.$t("form.file_name")))]
              ),
              _vm._v(" "),
              _c("div", { staticClass: "col-sm-8" }, [
                _c("input", {
                  directives: [
                    {
                      name: "model",
                      rawName: "v-model",
                      value: _vm.file_name,
                      expression: "file_name"
                    }
                  ],
                  staticClass: "form-control",
                  attrs: {
                    type: "text",
                    id: "file_name",
                    name: "file_name",
                    placeholder: _vm.$t("form.file_name")
                  },
                  domProps: { value: _vm.file_name },
                  on: {
                    input: function($event) {
                      if ($event.target.composing) {
                        return
                      }
                      _vm.file_name = $event.target.value
                    }
                  }
                })
              ])
            ])
          ])
        ],
        2
      ),
      _vm._v(" "),
      _c(
        "modal",
        {
          attrs: { show: _vm.showImage },
          on: {
            confirm: _vm.confirm,
            cancel: function($event) {
              _vm.showImage = false
            }
          }
        },
        [
          _c("template", { slot: "title" }, [
            _vm._v(_vm._s(_vm.$t("form.image")))
          ]),
          _vm._v(" "),
          _c("div", { staticClass: "col-sm-12 text-center" }, [
            _c("img", {
              staticClass: "preview-size",
              attrs: { src: _vm.preview_image }
            })
          ])
        ],
        2
      )
    ],
    1
  )
}
var staticRenderFns = []
render._withStripped = true
module.exports = { render: render, staticRenderFns: staticRenderFns }
if (false) {
  module.hot.accept()
  if (module.hot.data) {
    require("vue-hot-reload-api")      .rerender("data-v-eb55ec6c", module.exports)
  }
}

/***/ })

});
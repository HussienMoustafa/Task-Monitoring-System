"use strict";

function App(props) {
  return /*#__PURE__*/React.createElement("div", {
    className: "todoapp stack-large"
  }, /*#__PURE__*/React.createElement("h1", null, "TodoMatic"), /*#__PURE__*/React.createElement("form", null, /*#__PURE__*/React.createElement("h2", {
    className: "label-wrapper"
  }, /*#__PURE__*/React.createElement("label", {
    htmlFor: "new-todo-input",
    className: "label__lg"
  }, "What needs to be done?")), /*#__PURE__*/React.createElement("input", {
    type: "text",
    id: "new-todo-input",
    className: "input input__lg",
    name: "text",
    autoComplete: "off"
  }), /*#__PURE__*/React.createElement("button", {
    type: "submit",
    className: "btn btn__primary btn__lg"
  }, "Add")), /*#__PURE__*/React.createElement("div", {
    className: "filters btn-group stack-exception"
  }, /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn toggle-btn",
    "aria-pressed": "true"
  }, /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Show "), /*#__PURE__*/React.createElement("span", null, "all"), /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, " tasks")), /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn toggle-btn",
    "aria-pressed": "false"
  }, /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Show "), /*#__PURE__*/React.createElement("span", null, "Active"), /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, " tasks")), /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn toggle-btn",
    "aria-pressed": "false"
  }, /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Show "), /*#__PURE__*/React.createElement("span", null, "Completed"), /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, " tasks"))), /*#__PURE__*/React.createElement("h2", {
    id: "list-heading"
  }, "3 tasks remaining"), /*#__PURE__*/React.createElement("ul", {
    role: "list",
    className: "todo-list stack-large stack-exception",
    "aria-labelledby": "list-heading"
  }, /*#__PURE__*/React.createElement("li", {
    className: "todo stack-small"
  }, /*#__PURE__*/React.createElement("div", {
    className: "c-cb"
  }, /*#__PURE__*/React.createElement("input", {
    id: "todo-0",
    type: "checkbox",
    defaultChecked: true
  }), /*#__PURE__*/React.createElement("label", {
    className: "todo-label",
    htmlFor: "todo-0"
  }, "Eat")), /*#__PURE__*/React.createElement("div", {
    className: "btn-group"
  }, /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn"
  }, "Edit ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Eat")), /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn btn__danger"
  }, "Delete ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Eat")))), /*#__PURE__*/React.createElement("li", {
    className: "todo stack-small"
  }, /*#__PURE__*/React.createElement("div", {
    className: "c-cb"
  }, /*#__PURE__*/React.createElement("input", {
    id: "todo-1",
    type: "checkbox"
  }), /*#__PURE__*/React.createElement("label", {
    className: "todo-label",
    htmlFor: "todo-1"
  }, "Sleep")), /*#__PURE__*/React.createElement("div", {
    className: "btn-group"
  }, /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn"
  }, "Edit ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Sleep")), /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn btn__danger"
  }, "Delete ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Sleep")))), /*#__PURE__*/React.createElement("li", {
    className: "todo stack-small"
  }, /*#__PURE__*/React.createElement("div", {
    className: "c-cb"
  }, /*#__PURE__*/React.createElement("input", {
    id: "todo-2",
    type: "checkbox"
  }), /*#__PURE__*/React.createElement("label", {
    className: "todo-label",
    htmlFor: "todo-2"
  }, "Repeat")), /*#__PURE__*/React.createElement("div", {
    className: "btn-group"
  }, /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn"
  }, "Edit ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Repeat")), /*#__PURE__*/React.createElement("button", {
    type: "button",
    className: "btn btn__danger"
  }, "Delete ", /*#__PURE__*/React.createElement("span", {
    className: "visually-hidden"
  }, "Repeat"))))));
}

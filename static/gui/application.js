$(document).ready(function() {
  $('.add-input').click(function(evt) {
    evt.preventDefault();
    var parentElt = $(evt.target).parent();
    var elt = "<input name='" +
      evt.target.dataset['name'] +
      "' type='" +
      evt.target.dataset['type'] +
      "' class='form-control' aria-label='Small' aria-describedby='inputgroup-" +
      evt.target.dataset['name'] +
      "' placeholder='" +
      evt.target.dataset['placeholder'] +
      "'>"
    parentElt.after(
      "<div class='input-group input-group-sm mb-3'>" +
        "<div class='input-group-prepend'><span class='input-group-text' id='inputgroup-'>" + evt.target.dataset['name'] + "</span></div>" + elt +
      "</div>"
    )
  })
});

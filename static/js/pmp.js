$("[data-collapse-group]").on('show.bs.collapse', function () {
  var $this = $(this);
  var thisCollapseAttr = $this.attr('data-collapse-group');
  $("[data-collapse-group='" + thisCollapseAttr + "']").not($this).collapse('hide');
});

$("[data-collapse-group-2]").on('show.bs.collapse', function () {
  var $this = $(this);
  var thisCollapseAttr = $this.attr('data-collapse-group-2');
  $("[data-collapse-group-2='" + thisCollapseAttr + "']").not($this).collapse('hide');
});

$("[data-collapse-group-3]").on('show.bs.collapse', function () {
  var $this = $(this);
  var thisCollapseAttr = $this.attr('data-collapse-group-3');
  $("[data-collapse-group-3='" + thisCollapseAttr + "']").not($this).collapse('hide');
  $(".gym-collapsable").collapse();
});

$("[data-collapse-group-4]").on('show.bs.collapse', function () {
  var $this = $(this);
  var thisCollapseAttr = $this.attr('data-collapse-group-4');
  $("[data-collapse-group-4='" + thisCollapseAttr + "']").not($this).collapse('hide');
  $(".gym-collapsable").collapse();
});

$(document).ready(function(){
  $(".ld")[0].click(()=>{
    console.log("clicked");
  });
  document.getElementsByTagName("body")[0].classList.remove("loader");
  $("#dietgym").click(()=>{
    $("#workout-videos-tab").click();
  });
  $("#dsInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".ds-list").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
  $("#germanInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".german-course-ids").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $(".gdInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".gdList").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

});

function hideAll(element) {
  // $(".gym-collapsable").removeClass('show');
  $(".gdInput").val('').keyup();
  $(".tab-panel").hide();
  $(".tab-panel#"+element).show();
}
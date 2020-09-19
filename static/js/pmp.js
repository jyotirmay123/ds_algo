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

  // $('#daily-workouts').DataTable();
  // $('#food-recipe').DataTable();
  // $('#workout-videos').DataTable();
});

function hideAll() {
  $(".gym-collapsable").removeClass('show');
  $(".gdInput").val('').keyup();
}

// $("[data-collapse-group-3]").on('show.bs.collapse', function () {
//   var $this = $(this);
//   var thisCollapseAttr = $this.attr('data-collapse-group-3');
//   $("[data-collapse-group-3='" + thisCollapseAttr + "']").not($this).collapse('hide');
// });


// $('.make_bigger').click(function() {
//   $('.active').not(this).addClass('non_active-img');
//   $('.active').not(this).removeClass('active-img');
//   if ($(this).hasClass('active-img')) {
//     $(this).addClass('non_active-img');
//     $(this).removeClass('active-img');
//   } else {
//     $(this).removeClass('non_active-img');
//     $(this).addClass('active-img');
//   }
// });
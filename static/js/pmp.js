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
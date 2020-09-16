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
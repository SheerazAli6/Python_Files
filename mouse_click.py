<!DOCTYPE html>
<!-- saved from url=(0052)http://py3.codeskulptor.org/#user301_KydKtyqzUf_0.py -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title>CodeSkulptor</title>
    <link href="http://py3.codeskulptor.org/favicon.ico" rel="shortcut icon">


    <link rel="stylesheet" href="./mouse_click_files/jquery-ui.css">
    <link href="./mouse_click_files/css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" type="text/css" href="./mouse_click_files/codemirror.css">
    <link rel="stylesheet" type="text/css" href="./mouse_click_files/dialog.css">
    <link rel="stylesheet" type="text/css" href="./mouse_click_files/codeskulptor.css">
    <link rel="stylesheet" href="./mouse_click_files/bootstrap.min.css">

    <script type="text/javascript" src="./mouse_click_files/jquery.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery-ui.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery.form.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery.ui.touch-punch.min.js.download"></script>
    <script src="./mouse_click_files/js"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery.flot.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery.flot.axislabels.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/jquery.flot.orderbars.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/numeric-1.2.6.min.js.download"></script>

    <script src="./mouse_click_files/bootstrap.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/codemirror-compressed.js.download"></script>

    <script type="text/javascript" src="./mouse_click_files/skulpt.min.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/skulpt-stdlib.js.download"></script>
    <script type="text/javascript" src="./mouse_click_files/codeskulptor-compressed.js.download"></script>


<script type="text/javascript" charset="UTF-8" src="./mouse_click_files/common.js.download"></script><script type="text/javascript" charset="UTF-8" src="./mouse_click_files/util.js.download"></script><script type="text/javascript" charset="UTF-8" src="./mouse_click_files/stats.js.download"></script></head>

<body>

<div id="bodyWrapper">

    <h3 id="homeTab" class="h3 text-center">CodeSkulptor3</h3>

    <div id="mainBody">

        <!-- Anchor elements for load and download functionalities. -->
        <input type="file" id="localfile">
        <a id="dlhref" href="http://codeskulptor-user301.commondatastorage.googleapis.com/user301_KydKtyqzUf_0.py"></a>

        <div id="btnToolbarPortrait" class="text-center" style="display: none;">
            <button id="run" type="button" class="btn btn-warning runBtn">
                    <span class="glyphicon glyphicon-play" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Run</small></span>
            </button>
            <button type="button" class="btn btn-warning resetBtn">
                    <span class="glyphicon glyphicon-step-backward" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Reset</small></span>
            </button>
            <button type="button" class="btn btn-primary saveBtn" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Save the current Python code.">
                    <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Save</small></span>
            </button>
            <button type="button" class="btn btn-primary freshBtn" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Generate a new URL for this Python code.">
                    <span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>New URL</small></span>
            </button>
            <button type="button" class="btn btn-primary dlBtn" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Download a copy of the most recently Python code." disabled="">
                    <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Download</small></span>
            </button>
            <button type="button" class="btn btn-primary loadLocalBtn" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Load contents of a local file to CodeSkulptor.">
                    <span class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Load</small></span>
            </button>
            <a class="btn btn-info docsBtn" href="http://py3.codeskulptor.org/docs.html" target="_blank" role="button" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Read documentation about how to use Python and CodeSkulptor.">
                    <span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>Docs</small></span>
            </a>
            <a class="btn btn-info aboutBtn" href="http://py3.codeskulptor.org/about.html" target="_blank" role="button" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Learn more about CodeSkulptor.">
                    <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
                    <span class="hidden-xs"><small>About</small></span>
            </a>
            <span class="dropdown" style="display: none;">
              <button class="btn btn-danger dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">
                    <small><span class="badge numFrames"></span></small>
                    <span class="hidden-xs"><small>Frames</small></span>
              </button>
              <ul class="dropdown-menu dropdown-menu-right" role="menu" aria-labelledby="dropdownMenu1">

              </ul>
            </span>
        </div>

        <br>

        <div id="outputRow" class="row">

            <div id="btnToolbarLandscape" class="col-xs-1" style="display: block;">
                <div class="runTooltip" data-toggle="tooltip" data-placement="right" title="" data-original-title="Execute the Python program from the beginning.">
                    <button type="button" class="btn btn-warning runBtn">
                            <span class="glyphicon glyphicon-play" aria-hidden="true"></span>
                            <span class="hidden-xs hidden-sm hidden-md"><small>Run</small></span>
                    </button>
                </div>
                <button type="button" class="btn btn-warning resetBtn" data-toggle="tooltip" data-placement="right" title="" data-original-title="Stop the program and clear all output.">
                        <span class="glyphicon glyphicon-step-backward" aria-hidden="true"></span>
                        <span class="hidden-xs hidden-sm hidden-md"><small>Reset</small></span>
                </button>
                <button type="button" class="btn btn-primary saveBtn" data-toggle="tooltip" data-placement="right" title="" data-original-title="Save the current Python code.">
                        <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
                        <span class="hidden-xs hidden-sm hidden-md"><small>Save</small></span>
                </button>
                <button type="button" class="btn btn-primary freshBtn" data-toggle="tooltip" data-placement="right" title="" data-original-title="Generate a new URL for this Python code.">
                        <span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>
                        <span class="hidden-xs hidden-sm hidden-md"><small>New URL</small></span>
                </button>
                <button type="button" class="btn btn-primary dlBtn" data-toggle="tooltip" data-placement="right" title="" data-original-title="Download a copy of the most recently saved Python code." disabled="">
                        <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span>
                        <span class="hidden-xs hidden-sm hidden-md"><small>Download</small></span>
                </button>
                <button type="button" class="btn btn-primary loadLocalBtn" data-toggle="tooltip" data-placement="right" title="" data-original-title="Load contents of a local file to CodeSkulptor.">
                        <span class="glyphicon glyphicon-folder-open" aria-hidden="true"></span>
                        <span class="hidden-xs hidden-sm hidden-md"><small>Load</small></span>
                </button>
                <div data-toggle="tooltip" data-placement="right" title="" data-original-title="Read documentation about how to use Python and CodeSkulptor.">
                    <a class="btn btn-info docsBtn" href="http://py3.codeskulptor.org/docs.html" target="_blank" role="button">
                            <span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span>
                            <span class="hidden-xs hidden-sm hidden-md"><small>Docs</small></span>
                    </a>
                </div>
                <div data-toggle="tooltip" data-placement="right" title="" data-original-title="Learn more about CodeSkulptor.">
                    <a class="btn btn-info aboutBtn" href="http://py3.codeskulptor.org/about.html" target="_blank" role="button">
                            <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
                            <span class="hidden-xs hidden-sm hidden-md"><small>About</small></span>
                    </a>
                </div>

                <div class="dropdown" style="display: none;">
                  <button class="btn btn-danger dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-expanded="true">
                    <span class="badge numFrames">0</span>
                    <span class="hidden-xs hidden-sm hidden-md"><small>Frames</small></span>
                  </button>
                  <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">

                  </ul>
                </div>
            </div> <!-- /btnToolbarLandscape -->


            <div id="active" class="col-xs-11" style="width: 928px;">
                <div class="row row-no-gutter">

                    <div id="codeContainer" class="col-xs-6" style="width: 734px;">
                        <div class="cs-panel panel panel-primary">
                            <div class="panel-heading">Code</div>
                            <div id="codePanelBackground" class="panel-body" style="background-color: rgb(255, 255, 255);">
                                <form action="http://codeskulptor-user301.commondatastorage.googleapis.com/" method="post" enctype="multipart/form-data" id="codeform">
                                    <input type="hidden" name="key" id="keyid" value="user301_KydKtyqzUf_0.py">
                                    <input type="hidden" name="Content-Type" value="text/x-python">
                                    <input type="hidden" name="GoogleAccessId" id="googleid" value="GOOG6IFHB7AUBQLPX2JM">
                                    <input type="hidden" name="Policy" id="policy" value="eyJleHBpcmF0aW9uIjogIjIwMTgtMDgtMDFUMTI6MDA6MDAuMDAwWiIsCgogICJjb25kaXRpb25zIjogWwogICAgeyJidWNrZXQiOiAiY29kZXNrdWxwdG9yLXVzZXIzMDEifSwKICAgIFsic3RhcnRzLXdpdGgiLCAiJGtleSIsICJ1c2VyMzAxIl0sCiAgICBbImVxIiwgIiRDb250ZW50LVR5cGUiLCAidGV4dC94LXB5dGhvbiJdLAogICAgWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDY1NTM2XQogIF0KfQo=">
                                    <input type="hidden" name="Signature" id="signature" value="7msem1fLfqrYjvwJwSD2hlSUnsY=">
                                    <textarea id="code" name="file" style="display: none;"></textarea><div class="CodeMirror cm-s-default" style="height: 501px; background-color: rgb(255, 255, 255);"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 184px; left: 462.891px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true" style="bottom: 0px; display: block;"><div style="min-width: 1px; height: 566px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true" style="right: 0px; left: 0px;"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true" style="height: 17px; width: 17px;"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 30px; margin-bottom: -17px; border-right-width: 13px; min-height: 566px; min-width: 631px; padding-right: 17px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 432.891px; top: 180px; height: 18px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">simplegui</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">math</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">width</span> = <span class="cm-number">500</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">height</span> = <span class="cm-number">400</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">bol_position</span> = [<span class="cm-variable">width</span> <span class="cm-operator">/</span> <span class="cm-number">2</span>, <span class="cm-variable">height</span> <span class="cm-operator">/</span> <span class="cm-number">2</span>]</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">bol_radious</span> = <span class="cm-number">20</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">bol_colour</span> = <span class="cm-string">"red"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">distance</span>(<span class="cm-variable">p</span>,<span class="cm-variable">q</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">math</span>.<span class="cm-property">sqrt</span>((<span class="cm-variable">p</span>[<span class="cm-number">0</span>] <span class="cm-operator">-</span> <span class="cm-variable">q</span>[<span class="cm-number">0</span>]) <span class="cm-operator">**</span> <span class="cm-number">2</span> <span class="cm-operator">+</span> <span class=" CodeMirror-matchingbracket">(</span><span class="cm-variable">p</span>[<span class="cm-number">1</span>] <span class="cm-operator">-</span> <span class="cm-variable">q</span>[<span class="cm-number">1</span>]<span class=" CodeMirror-matchingbracket">)</span> <span class="cm-operator">**</span> <span class="cm-number">2</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">13</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">draw</span>(<span class="cm-variable">canvas</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">14</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">canvas</span>.<span class="cm-property">draw_circle</span>(<span class="cm-variable">bol_position</span>,<span class="cm-variable">bol_radious</span> , <span class="cm-number">2</span> , <span class="cm-string">"Orange"</span> , <span class="cm-variable">bol_colour</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">15</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">16</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">click</span>(<span class="cm-variable">pos</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">17</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">global</span> <span class="cm-variable">bol_position</span>,<span class="cm-variable">bol_colour</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">18</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">if</span>(<span class="cm-variable">distance</span>(<span class="cm-variable">pos</span>,<span class="cm-variable">bol_position</span>) <span class="cm-operator">&lt;</span> <span class="cm-variable">bol_radious</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">19</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">bol_colour</span> = <span class="cm-string">"Green"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">20</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">else</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">21</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">bol_position</span> = <span class="cm-builtin">list</span>(<span class="cm-variable">pos</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">22</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">bol_colour</span> = <span class="cm-string">"red"</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">23</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">24</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">frame</span> = <span class="cm-variable">simplegui</span>.<span class="cm-property">create_frame</span>(<span class="cm-string">"This Is Mouse Click Programme"</span> , <span class="cm-variable">width</span> , <span class="cm-variable">height</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">25</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">frame</span>.<span class="cm-property">set_canvas_background</span>(<span class="cm-string">"white"</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">26</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">frame</span>.<span class="cm-property">set_draw_handler</span>(<span class="cm-variable">draw</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">27</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">frame</span>.<span class="cm-property">set_mouseclick_handler</span>(<span class="cm-variable">click</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">28</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">29</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">30</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">frame</span>.<span class="cm-property">start</span>()</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">31</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 566px;"></div><div class="CodeMirror-gutters" style="height: 579px;"><div class="CodeMirror-gutter fold-gutter"></div><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div></div></div></div>
                                </form>
                            </div>
                        </div>


                    </div>

                    <div id="outputContainer" class="col-xs-6" style="width: 170px;">

                        <div id="splitbar" style="height: 534px; cursor: auto;">
                          <div id="grip"></div>
                        </div>

                        <div class="cs-panel panel panel-primary">
                            <div class="panel-heading">Output</div>
                            <div id="outputPanel" class="panel-body" style="height: 501px;">
                                <div id="console"></div>
                            </div>
                        </div>
                    </div>

                </div>

            </div> <!-- /active -->

        </div> <!-- /row -->

    </div> <!-- /mainBody -->

</div> <!-- /bodyWrapper -->


</body></html>
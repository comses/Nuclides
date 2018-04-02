





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-KDZfnHRZjn4xEe2VuPe5iA8c+O1aNoowrYTe3DQQR97UQDzf5HZ15My/ytImCLmX5X6kBM8kwtuUVj5H+DOZbA==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-7d09971c51977b60c6626362003ef38a.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-g2U5nfPqM0P4RbTRKgDvhuXPJVejnANdcCwXQd8scIlHyTrqIu6uIeM42oTLSXxYW7rsg1VzEId21Irp9GdS3A==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-c80e46361da241076cf7df5a359801c7.css" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>medland/strat_column.py at master_deprecated · comses/medland</title>
    <meta name="description" content="GitHub is where people build software. More than 27 million people use GitHub to discover, fork, and contribute to over 80 million projects.">
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/6599264?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="comses/medland" /><meta property="og:url" content="https://github.com/comses/medland" /><meta property="og:description" content="Medland project repository (http://medland.asu.edu)" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjYwMzY4OTMxOmU5NGM2MWIzOTk0Mzk1NzliMTczNWIxM2I2MDVlOTUxYWY2ODE5ZDgwNTFmYmE1Y2E4OWVjZmY5ODA4MWM4YTk=--8b86e9b093545c372377d933984da3a56a9a49a0">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="DBF0:5D1A:AED28:13E1B8:5AC276FE" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="DBF0:5D1A:AED28:13E1B8:5AC276FE" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="12808168" /><meta name="octolytics-actor-login" content="nick-gauthier" /><meta name="octolytics-actor-hash" content="f168bb633435062240ef69fb3bd01e4517e915052cd524f4b526bc6bb2bfa0c7" />
<meta name="hydro-events-url" content="https://github.com/hydro_browser_events" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="nick-gauthier">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YmY4N2I4YWM5YmY3NmI3MGRhOTIxYjdjMGJiNjY4YTJhMjI5ODhmMzRkYzY3OGEwZmJiMTlmM2I2Y2EzYjQ0OHx7InJlbW90ZV9hZGRyZXNzIjoiMTQ5LjE2OS44MS40MSIsInJlcXVlc3RfaWQiOiJEQkYwOjVEMUE6QUVEMjg6MTNFMUI4OjVBQzI3NkZFIiwidGltZXN0YW1wIjoxNTIyNjkzOTA0LCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS,MARKETPLACE_INSIGHTS,MARKETPLACE_INSIGHTS_CONVERSION_PERCENTAGES">

  <meta name="html-safe-nonce" content="abb7a1811420d74739b7a2ffeb717a57d86a658d">

  <meta http-equiv="x-pjax-version" content="7f8bd3ca807c71aec231464e556f918b">
  

      <link href="https://github.com/comses/medland/commits/master_deprecated.atom?token=AMNv6ANBudbF8X-k_nBif3QnEDVnCIVxks64z6mQwA%3D%3D" rel="alternate" title="Recent Commits to medland:master_deprecated" type="application/atom+xml">

  <meta name="description" content="Medland project repository (http://medland.asu.edu)">
  <meta name="go-import" content="github.com/comses/medland git https://github.com/comses/medland.git">

  <meta name="octolytics-dimension-user_id" content="6599264" /><meta name="octolytics-dimension-user_login" content="comses" /><meta name="octolytics-dimension-repository_id" content="22450770" /><meta name="octolytics-dimension-repository_nwo" content="comses/medland" /><meta name="octolytics-dimension-repository_public" content="false" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="22450770" /><meta name="octolytics-dimension-repository_network_root_nwo" content="comses/medland" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/comses/medland/blob/master_deprecated/digital_proxy_model/strat_column.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

<link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 container-lg">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scoped-search-url="/comses/medland/search" data-unscoped-search-url="/search" action="/comses/medland/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
    <label class="form-control header-search-wrapper  js-chromeless-input-container">
        <a class="header-search-scope no-underline" href="/comses/medland/blob/master_deprecated/digital_proxy_model/strat_column.py">This repository</a>
      <input type="text"
        class="form-control header-search-input  js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s,/"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off"
        >
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
                <li>
                  <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace" href="/marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:12808168" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="comses/medland">This repository</span>
  </div>
    <a class="dropdown-item" href="/comses/medland/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@nick-gauthier" class="avatar float-left mr-1" src="https://avatars3.githubusercontent.com/u/12808168?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">nick-gauthier</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/nick-gauthier" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/nick-gauthier?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="BqsRkiGam7E0OP3icSMU7WTTb1YPywUyieJrcG3VV/yfZ8GLFfpIxQJfXN7t7G81sG3A7250beFfDZp8n4r+8A==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="uwgyCZgS3GsW0h9G0uP9zzp06/WNUqBZemD+xOD6N0kixOIQrHIPHyC1vnpOLIYX7spETOztyIqsjw/IEqWeRQ==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      





  



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="1Qudwx6qHCjuySkxfryhtfKWFxg7JfHJd3GrUYI6XoZCkQGw6U3FQp44DUDfFSGRb7QilAQT376gdIL3RLrk6A==" />      <input type="hidden" name="repository_id" id="repository_id" value="22450770" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/comses/medland/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Unwatch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/comses/medland/watchers"
            aria-label="9 users are watching this repository">
            9
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" checked="checked" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/comses/medland/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="uHrqE0hGncYN37aGrXcMJBHKCZiMDHcinL3H2J0wHQ+rLfZTV0OuagxWbYRODfGoacuBmRzaDPkPEnBHPmJWEQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar comses/medland"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/comses/medland/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/comses/medland/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="V8WNjVp0nq4KA0KxabwJLYj3i4PHWNnvkP9KbwljiHmk0g0HFp8b1HyoFGISrTgjl2LBzDFOkZRjZjLZ5nJJZA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star comses/medland"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/comses/medland/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of comses/medland to your account"
              aria-label="Fork your own copy of comses/medland to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/comses/medland/fork?fragment=1">
              <img alt="Loading" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" height="64" />
            </include-fragment>
          </div>

    <a href="/comses/medland/network" class="social-count"
       aria-label="2 users forked this repository">
      2
    </a>
  </li>
</ul>

      <h1 class="private ">
  <svg class="octicon octicon-lock" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 13H3v-1h1v1zm8-6v7c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h1V4c0-2.2 1.8-4 4-4s4 1.8 4 4v2h1c.55 0 1 .45 1 1zM3.8 6h4.41V4c0-1.22-.98-2.2-2.2-2.2-1.22 0-2.2.98-2.2 2.2v2H3.8zM11 7H2v7h9V7zM4 8H3v1h1V8zm0 2H3v1h1v-1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/comses">comses</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/comses/medland">medland</a></strong>
    <span class="Label Label--outline v-align-middle">Private</span>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /comses/medland/tree/master_deprecated" href="/comses/medland/tree/master_deprecated">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /comses/medland/issues" href="/comses/medland/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /comses/medland/pulls" href="/comses/medland/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /comses/medland/projects" href="/comses/medland/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /comses/medland/wiki" href="/comses/medland/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /comses/medland/pulse" href="/comses/medland/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/comses/medland/blob/6ab47b971a35fb88f3a1e0a880f7a323e4133df5/digital_proxy_model/strat_column.py">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:1ec214a6cae6540768f4f84fb64bf76f -->

  <div class="file-navigation">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title="master_deprecated"
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master_depreca…</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/comses/medland/blob/master_deprecated/digital_proxy_model/strat_column.py"
               data-name="master_deprecated"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master_deprecated
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/comses/medland/blob/master/digital_proxy_model/strat_column.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" action="/comses/medland/branches" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="tSsaZ8H4KInafvjPBDvbY5mrI4CL8nryDyQUC/UmcEahhM/bR2a/QzLcLsbQQXjrge8+3aKXAthSpUJTgv8CNw==" />
          <svg class="octicon octicon-git-branch select-menu-item-icon" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 5c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v.3c-.02.52-.23.98-.63 1.38-.4.4-.86.61-1.38.63-.83.02-1.48.16-2 .45V4.72a1.993 1.993 0 0 0-1-3.72C.88 1 0 1.89 0 3a2 2 0 0 0 1 1.72v6.56c-.59.35-1 .99-1 1.72 0 1.11.89 2 2 2 1.11 0 2-.89 2-2 0-.53-.2-1-.53-1.36.09-.06.48-.41.59-.47.25-.11.56-.17.94-.17 1.05-.05 1.95-.45 2.75-1.25S8.95 7.77 9 6.73h-.02C9.59 6.37 10 5.73 10 5zM2 1.8c.66 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2C1.35 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2zm0 12.41c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm6-8c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master_deprecated’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master_deprecated">
            <input type="hidden" name="path" id="path" value="digital_proxy_model/strat_column.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/MMLv1.0/digital_proxy_model/strat_column.py"
              data-name="MMLv1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="MMLv1.0">
                MMLv1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/MML_v5.0/digital_proxy_model/strat_column.py"
              data-name="MML_v5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="MML_v5.0">
                MML_v5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/MML_v3.0/digital_proxy_model/strat_column.py"
              data-name="MML_v3.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="MML_v3.0">
                MML_v3.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/MML_v1.2/digital_proxy_model/strat_column.py"
              data-name="MML_v1.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="MML_v1.2">
                MML_v1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/Land_v3.0/digital_proxy_model/strat_column.py"
              data-name="Land_v3.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="Land_v3.0">
                Land_v3.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/Land_v2.0/digital_proxy_model/strat_column.py"
              data-name="Land_v2.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="Land_v2.0">
                Land_v2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/Land_v1.2/digital_proxy_model/strat_column.py"
              data-name="Land_v1.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="Land_v1.2">
                Land_v1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/Land_v1.0/digital_proxy_model/strat_column.py"
              data-name="Land_v1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="Land_v1.0">
                Land_v1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/KIBv1.0/digital_proxy_model/strat_column.py"
              data-name="KIBv1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="KIBv1.0">
                KIBv1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/KIB_v1.2/digital_proxy_model/strat_column.py"
              data-name="KIB_v1.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="KIB_v1.2">
                KIB_v1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/comses/medland/tree/KIB_v1.1/digital_proxy_model/strat_column.py"
              data-name="KIB_v1.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="KIB_v1.1">
                KIB_v1.1
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/comses/medland/find/master_deprecated"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <clipboard-copy
            for="blob-path"
            aria-label="Copy file path to clipboard"
            class="btn btn-sm BtnGroup-item tooltipped tooltipped-s"
            copied-label="Copied!">
        Copy path
      </clipboard-copy>
    </div>
    <div id="blob-path" class="breadcrumb">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/comses/medland/tree/master_deprecated"><span>medland</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/comses/medland/tree/master_deprecated/digital_proxy_model"><span>digital_proxy_model</span></a></span><span class="separator">/</span><strong class="final-path">strat_column.py</strong>
    </div>
  </div>


  <include-fragment src="/comses/medland/contributors/master_deprecated/digital_proxy_model/strat_column.py" class="commit-tease">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>

  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/comses/medland/raw/master_deprecated/digital_proxy_model/strat_column.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/comses/medland/blame/master_deprecated/digital_proxy_model/strat_column.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/comses/medland/commits/master_deprecated/digital_proxy_model/strat_column.py">History</a>
    </div>


          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/comses/medland/edit/master_deprecated/digital_proxy_model/strat_column.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="sFD0gz4a03r58p61FOjAwQNRI6YcmrJ8GGC8Bf0/IYBknQrFkRL5N0HqWzcc7x/LMgQYAVYAedSJnrb3I/M9kA==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Edit this file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/comses/medland/delete/master_deprecated/digital_proxy_model/strat_column.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="KQcrm2Q0hrjusGVh9WbwH4JbupbUN5h9zP7Pn4cymLUIgelENuOAB5VQkUX7rYUtTg9z9LEuuGWk6mb+zQFYSg==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      276 lines (257 sloc)
      <span class="file-info-divider"></span>
    18.8 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">exit</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>This script requires the Python package <span class="pl-cce">\&#39;</span>NumPy<span class="pl-cce">\&#39;</span>. Please install that and try again.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">exit</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>This script requires the Python package <span class="pl-cce">\&#39;</span>Pandas<span class="pl-cce">\&#39;</span>. Please install that and try again.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> plt</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">exit</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>This script requires the Python package <span class="pl-cce">\&#39;</span>MatPlotLib<span class="pl-cce">\&#39;</span>. Please install that and try again.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> seaborn <span class="pl-k">as</span> sns</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">exit</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>This script requires the Python package <span class="pl-cce">\&#39;</span>Seaborn<span class="pl-cce">\&#39;</span>. Please install that and try again.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> grass.script <span class="pl-k">as</span> grass</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">exit</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>You must have GRASS GIS installed, and be in a GRASS session to run this script<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">int</span>(grass.version()[<span class="pl-s"><span class="pl-pds">&#39;</span>version<span class="pl-pds">&#39;</span></span>].split(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>]) <span class="pl-k">&lt;</span> <span class="pl-c1">7</span>:</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">    grass.fatal(<span class="pl-s"><span class="pl-pds">&quot;</span>You must be in GRASS version 7.0.1 or higher to run this script!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> tempfile, math</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>################ SET UP THESE VALUES ####################</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#########################################################</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">RunLength <span class="pl-k">=</span> <span class="pl-c1">300</span> <span class="pl-c"><span class="pl-c">#</span>number of years the simulation ran for</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">digits <span class="pl-k">=</span> <span class="pl-c1">3</span> <span class="pl-c"><span class="pl-c">#</span>number of digits that simulation year numbers are padded to</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">prefix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>120psf<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">coor <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>727195.790391, 4285699.45461<span class="pl-pds">&quot;</span></span> <span class="pl-c"><span class="pl-c">#</span> location(s) at which to take a virtual sediment core</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">outprefix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>P2<span class="pl-pds">&quot;</span></span> <span class="pl-c"><span class="pl-c">#</span> A prefix for all output files.</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">baseinterval <span class="pl-k">=</span> <span class="pl-c1">0.001</span> <span class="pl-c"><span class="pl-c">#</span> the depth intervals at which to collect proxies (default is 1mm)</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">dispinterval <span class="pl-k">=</span> <span class="pl-c1">100</span> <span class="pl-c"><span class="pl-c">#</span> the number of depth intervals to amalgamate as the interval for the plot of proxies at the last year (default is 10cm)</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">miny <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1.25</span> <span class="pl-c"><span class="pl-c">#</span> optional minimum y value for the output stratigraphy plot</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">proxyscale <span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>linear<span class="pl-pds">&#39;</span></span> <span class="pl-c"><span class="pl-c">#</span> Scale for the x axis of the output proxies plot. &#39;log&#39; or &#39;linear&#39;</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#######</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Gathering data files...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">mapset <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.mapset<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>lp<span class="pl-pds">&#39;</span></span>).strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)<span class="pl-c"><span class="pl-c">#</span>grab mapset to constrain searches</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">elevmaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*Elevation_Map*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">depthmaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*Soil_Depth_Map*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)  </td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">deltamaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*ED_rate*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)  </td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">lcovmaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*Landcover_Map*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">farmingmaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*Farming_Impacts_Map*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">grazingmaps <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>g.list<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>m<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>*<span class="pl-c1">%s</span>*Gazing_Impacts_Map*<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> prefix, <span class="pl-v">separator</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>, <span class="pl-v">mapset</span> <span class="pl-k">=</span> mapset).strip().split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> we will need the initial landcover map for the charcoal calcualtions.</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">initlcov <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>init_veg@PERMANENT<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">basinmap <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>TEST_BASIN<span class="pl-pds">&quot;</span></span> <span class="pl-c"><span class="pl-c">#</span> We are just gonna use a single overarching basin map for now.</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>############################################################</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>############################################################</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># PREPARE FOR PROXY MODELING</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> generate base flow accumulation and direction maps from the DEMs in the list</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>n = 0</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>basinmaps = []</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>for elev in elevmaps:</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    n += 1</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    grass.run_command(&quot;r.watershed&quot;, quiet=True, overwrite=True, elevation=elevmaps[0], accumulation=&quot;Temporary_flacc&quot;, drainage=&quot;Temporary_fldr&quot;)</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    # delineate the uplope catchment basin</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    basinmap = &quot;Temporary_catchment_basin_%s&quot; % str(n).zfill(4)</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    grass.run_command(&quot;r.water.outlet&quot;, quiet=True, overwrite=True, input=&quot;Temporary_fldr&quot;, output=basinmap, coordinates=coor)</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    basinmaps.append(basinmap)</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>calculate base areal scalars</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">reg <span class="pl-k">=</span> grass.region() <span class="pl-c"><span class="pl-c">#</span> grab region info, including nsres and ewres</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">m2percell <span class="pl-k">=</span> reg[<span class="pl-s"><span class="pl-pds">&#39;</span>nsres<span class="pl-pds">&#39;</span></span>] <span class="pl-k">*</span> reg[<span class="pl-s"><span class="pl-pds">&#39;</span>ewres<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">cm2percell <span class="pl-k">=</span> reg[<span class="pl-s"><span class="pl-pds">&#39;</span>nsres<span class="pl-pds">&#39;</span></span>] <span class="pl-k">*</span> reg[<span class="pl-s"><span class="pl-pds">&#39;</span>ewres<span class="pl-pds">&#39;</span></span>] <span class="pl-k">*</span> <span class="pl-c1">10000</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> grab the number of upslope cells in the current basin</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">upslopecells <span class="pl-k">=</span> <span class="pl-c1">float</span>(grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>r.stats<span class="pl-pds">&#39;</span></span>, <span class="pl-v">quiet</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>cn<span class="pl-pds">&#39;</span></span>, <span class="pl-v">input</span><span class="pl-k">=</span>basinmap, <span class="pl-v">nsteps</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>).strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">scalar <span class="pl-k">=</span> math.pow((upslopecells <span class="pl-k">*</span> m2percell), <span class="pl-k">-</span><span class="pl-c1">0.01</span> ) <span class="pl-c"><span class="pl-c">#</span>scales basin average readings to the size of the basin. Accounts for time averaging and loss due to localized up-basin sinks.</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>change landcover maps to proxy of phytoliths for grasses</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&#39;</span>Generating grasses phytolith densities.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>tphytomaps = []</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>sphytomaps = []</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">gphytomaps <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">avphytos <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> lcovmap, elevmap, deltamap <span class="pl-k">in</span> <span class="pl-c1">zip</span>(lcovmaps, elevmaps, deltamaps):</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>Grasses DATA come from Fredlund and Tieszen 1994 for mixed grassland. Annual production of 2g/m2 of opaline grass phytoliths.</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    gphyto <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_insitu_grassphytos_<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (outprefix,lcovmap.split(<span class="pl-s"><span class="pl-pds">&#39;</span>_Landcover<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])    </td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    grass.mapcalc(<span class="pl-s"><span class="pl-pds">&quot;</span>$<span class="pl-c1">{phytomap}</span> = eval(a=nsres()*ewres()*2, b=graph($<span class="pl-c1">{lcovmap}</span>, 0,0.1, 5,1, 50,0.4), a*b)<span class="pl-pds">&quot;</span></span>, <span class="pl-v">overwrite</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">quiet</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">phytomap</span> <span class="pl-k">=</span> gphyto, <span class="pl-v">lcovmap</span> <span class="pl-k">=</span> lcovmap) <span class="pl-c"><span class="pl-c">#</span> modify yearly phytolith deposition for pure grassland by the actual landcover mixture (perecntage of grass in succession stage), and then scale to size of raster cel. This map is then g/cell of grass phytos.</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    gphytostats <span class="pl-k">=</span> grass.parse_command(<span class="pl-s"><span class="pl-pds">&#39;</span>r.univar<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>, <span class="pl-v">map</span><span class="pl-k">=</span>gphyto, <span class="pl-v">zones</span><span class="pl-k">=</span>basinmap) <span class="pl-c"><span class="pl-c">#</span> grab stats for average phytolith concentration</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    avphytos.append(<span class="pl-c1">float</span>(gphytostats[<span class="pl-s"><span class="pl-pds">&#39;</span>mean<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">*</span> scalar)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    gphytomaps.append(gphyto)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>change farming map to charcoal map</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Generating charcoal densities.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span><span class="pl-k">NOTE</span>: The following has landcover values HARDCODED to Mediterranean values. When reparammeterizing for non-Mediterranean environments, these will need to be recoded.</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">recodeto <span class="pl-k">=</span> tempfile.NamedTemporaryFile()</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> set up loop to create charcoal maps</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">charcoalmaps <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">averagecharc <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> n, lcovmap, farmingmap <span class="pl-k">in</span> <span class="pl-c1">zip</span>(<span class="pl-c1">range</span>(<span class="pl-c1">len</span>(lcovmaps)),lcovmaps, farmingmaps):</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    charcoalmap <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_insitu_charcoal_<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (outprefix,lcovmap.split(<span class="pl-s"><span class="pl-pds">&#39;</span>_Landcover<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> The code below uses graphing functions in mapcalc to translate veg type into above ground biomass (kg/sq m) and percentage of biomass that becomes charcoal, and then multiplying those two to find amount of charcoal produced (kg/sqm), and converting that into pieces per cell (note these are only for larger macro-charcoal between 400-600um). This last conversion is: (Kg charcoal * %charcoal in large size class * density of charcoal) / ( conversion rate from volume to #spherical particles * conversion from kg to g) .</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> n <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        lc <span class="pl-k">=</span> initlcov <span class="pl-c"><span class="pl-c">#</span>Calculate the standing biomass map (kg/sq m) based on year 0 veg, but year 1 farming</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        lc <span class="pl-k">=</span> lastlcov <span class="pl-c"><span class="pl-c">#</span>Calculate the standing biomass map (kg/sq m) based on last year veg, but this year&#39;s farming</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    grass.mapcalc(<span class="pl-s"><span class="pl-pds">&quot;</span>$<span class="pl-c1">{charcoal}</span>=eval(biomass=graph($<span class="pl-c1">{lcov}</span>, 0,0, 7,0.1, 18.5,0.66, 35,0.74, 50,1.95), pcntcharc=graph($<span class="pl-c1">{lcov}</span>, 0,0, 5,0.0048, 18.5,0.0101, 50,0.0325), if(isnull($<span class="pl-c1">{farmingmap}</span>), 0, ((biomass * pcntcharc * 0.0267 * 0.5) / (0.00011304 * 1000))) )<span class="pl-pds">&quot;</span></span>, <span class="pl-v">quiet</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">overwrite</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">lcov</span><span class="pl-k">=</span>lc, <span class="pl-v">charcoal</span><span class="pl-k">=</span>charcoalmap, <span class="pl-v">farmingmap</span><span class="pl-k">=</span>farmingmap)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    lastlcov <span class="pl-k">=</span> lcovmap <span class="pl-c"><span class="pl-c">#</span>save current lcov to use next year</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    charcoalmaps.append(charcoalmap) <span class="pl-c"><span class="pl-c">#</span> save name of charcoal map to use later</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    charcstats <span class="pl-k">=</span> grass.parse_command(<span class="pl-s"><span class="pl-pds">&#39;</span>r.univar<span class="pl-pds">&#39;</span></span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>g<span class="pl-pds">&#39;</span></span>, <span class="pl-v">map</span><span class="pl-k">=</span>charcoalmap, <span class="pl-v">zones</span><span class="pl-k">=</span>basinmap)</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    averagecharc.append(<span class="pl-c1">float</span>(charcstats[<span class="pl-s"><span class="pl-pds">&#39;</span>mean<span class="pl-pds">&#39;</span></span>]) <span class="pl-k">*</span> scalar)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    if charcstats.has_key(&#39;mean&#39;):</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        averagecharc.append(float(charcstats[&#39;mean&#39;]) * scalar)</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    else: # basin is very small, and/or no upstream charcoal deposits. This would create an empty stats dict, so just use 0 to avoid &quot;KeyError&quot; troubles</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        averagecharc.append(0)</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">recodeto.close() <span class="pl-c"><span class="pl-c">#</span> close and delete temporary rules file</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>change impact maps to artifact densities</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&#39;</span>Generating artifact densities.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">artifactmaps <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> farmingmap, grazingmap <span class="pl-k">in</span> <span class="pl-c1">zip</span>(farmingmaps, grazingmaps):</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    grass.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span>r.surf.random<span class="pl-pds">&quot;</span></span>, <span class="pl-v">quiet</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">overwrite</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>i<span class="pl-pds">&#39;</span></span>, <span class="pl-v">max</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">output</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Temporary_random_surface<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">    artifactmap <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_Artifact_densities_<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (outprefix,farmingmap.split(<span class="pl-s"><span class="pl-pds">&#39;</span>_Farming_Impacts_Map<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    grass.mapcalc(<span class="pl-s"><span class="pl-pds">&quot;</span>$<span class="pl-c1">{artifactmap}</span>=if(isnull($<span class="pl-c1">{farmingmap}</span>) &amp;&amp; isnull($<span class="pl-c1">{grazingmap}</span>), 0, if(isnull($<span class="pl-c1">{grazingmap}</span>), $<span class="pl-c1">{randmap}</span>+2, $<span class="pl-c1">{randmap}</span>))<span class="pl-pds">&quot;</span></span>, <span class="pl-v">overwrite</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">quiet</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">artifactmap</span><span class="pl-k">=</span>artifactmap, <span class="pl-v">farmingmap</span><span class="pl-k">=</span>farmingmap, <span class="pl-v">grazingmap</span><span class="pl-k">=</span>grazingmap, <span class="pl-v">randmap</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Temporary_random_surface<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">    artifactmaps.append(artifactmap)</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>now build a pandas dataframe to hold the yearly information about elevation changes and various proxy information, etc.</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>clean up temporary maps</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">grass.run_command(<span class="pl-s"><span class="pl-pds">&quot;</span>g.remove<span class="pl-pds">&quot;</span></span>, <span class="pl-v">quiet</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">flags</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>f<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>rast<span class="pl-pds">&#39;</span></span>, <span class="pl-v">pattern</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Temporary*<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Compiling yearly depth changes and raw proxy amounts...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">l <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(RunLength):</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    elev, delta, phyto, artifacts, charcoal, sdepth <span class="pl-k">=</span> grass.read_command(<span class="pl-s"><span class="pl-pds">&#39;</span>r.what<span class="pl-pds">&#39;</span></span>, <span class="pl-v">map</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>,<span class="pl-pds">&quot;</span></span>.join((elevmaps[i], deltamaps[i], gphytomaps[i], artifactmaps[i], charcoalmaps[i], depthmaps[i])), <span class="pl-v">separator</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>,<span class="pl-pds">&quot;</span></span>, <span class="pl-v">coordinates</span> <span class="pl-k">=</span> coor).strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>).split(<span class="pl-s"><span class="pl-pds">&quot;</span>,<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">3</span>:<span class="pl-c1">9</span>]</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">    l.append({<span class="pl-s"><span class="pl-pds">&#39;</span>Year<span class="pl-pds">&#39;</span></span>: i, <span class="pl-s"><span class="pl-pds">&#39;</span>Elevation<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">float</span>(elev), <span class="pl-s"><span class="pl-pds">&#39;</span>Soildepth<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">float</span>(sdepth), <span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">float</span>(delta), <span class="pl-s"><span class="pl-pds">&#39;</span>InSitu Grass Phytoliths<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">float</span>(phyto) <span class="pl-k">/</span> cm2percell, <span class="pl-s"><span class="pl-pds">&quot;</span>Scaled Basin-Average Grass Phytoliths<span class="pl-pds">&quot;</span></span>: <span class="pl-c1">float</span>(avphytos[i]) <span class="pl-k">/</span> cm2percell, <span class="pl-s"><span class="pl-pds">&quot;</span>InSitu Charcoal<span class="pl-pds">&quot;</span></span>: <span class="pl-c1">float</span>(charcoal) <span class="pl-k">/</span> cm2percell, <span class="pl-s"><span class="pl-pds">&quot;</span>Scaled Basin-Average Charcoal<span class="pl-pds">&quot;</span></span>:<span class="pl-c1">float</span>(averagecharc[i]) <span class="pl-k">/</span> cm2percell, <span class="pl-s"><span class="pl-pds">&#39;</span>Artifacts<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">int</span>(artifacts) <span class="pl-k">/</span> cm2percell})</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">layers <span class="pl-k">=</span> pd.DataFrame(l)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">initdepth <span class="pl-k">=</span> layers.Soildepth[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">layers[<span class="pl-s"><span class="pl-pds">&quot;</span>Cumsum<span class="pl-pds">&quot;</span></span>] <span class="pl-k">=</span> layers.Delta.cumsum()<span class="pl-k">+</span>initdepth <span class="pl-c"><span class="pl-c">#</span>calculate cumulative sum</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">layers.set_index(<span class="pl-s"><span class="pl-pds">&#39;</span>Year<span class="pl-pds">&#39;</span></span>, <span class="pl-v">inplace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>) <span class="pl-c"><span class="pl-c">#</span> first move the &quot;year&quot; column to be the index (1-RunLength)</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">layers.T.to_csv(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_CumED.csv<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix)</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>set up new dataframe to contain results and run a loop through the stratagraphic data to make &quot;real&quot; layers </span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Deriving temporal stratigraphy...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">stratigraphy <span class="pl-k">=</span> pd.DataFrame({y:np.arange(RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>) <span class="pl-k">for</span> y <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Year<span class="pl-pds">&quot;</span></span>]}) <span class="pl-c"><span class="pl-c">#</span>set up new dataframe to contain results of stratigraphic simulation</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">stratigraphy.set_index(<span class="pl-s"><span class="pl-pds">&#39;</span>Year<span class="pl-pds">&#39;</span></span>, <span class="pl-v">inplace</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>) <span class="pl-c"><span class="pl-c">#</span> first move the &quot;year&quot; column to be the index</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">stratigraphy[<span class="pl-s"><span class="pl-pds">&quot;</span>Stratum0<span class="pl-pds">&quot;</span></span>] <span class="pl-k">=</span> initdepth <span class="pl-c"><span class="pl-c">#</span> add a column for the base soil (stratum 0)</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> idx, row <span class="pl-k">in</span> layers.iterrows(): <span class="pl-c"><span class="pl-c">#</span> run a loop through the stratagraphic data to make &quot;real&quot; layers </span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> idx <span class="pl-k">==</span> <span class="pl-c1">0</span>: <span class="pl-c"><span class="pl-c">#</span> Set up the pre-run soil-depth</span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        stratigraphy[<span class="pl-s"><span class="pl-pds">&quot;</span>Stratum0<span class="pl-pds">&quot;</span></span>][idx:RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">=</span> initdepth <span class="pl-c"><span class="pl-c">#</span> save current depth at this year for the stratum (and fill forward in time)</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        old_delta <span class="pl-k">=</span> <span class="pl-c1">0</span> <span class="pl-c"><span class="pl-c">#</span> set up &quot;old_delta&quot; variable</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        stratum <span class="pl-k">=</span> <span class="pl-c1">0</span> <span class="pl-c"><span class="pl-c">#</span> set up &quot;stratum&quot; variable</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        currentdepth <span class="pl-k">=</span> initdepth</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        currentdepth <span class="pl-k">+=</span> row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-c"><span class="pl-c">#</span> figure out where the surface is this year</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&gt;=</span> <span class="pl-c1">0</span>: <span class="pl-c"><span class="pl-c">#</span> Deposition happened this year...</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> old_delta <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>: <span class="pl-c"><span class="pl-c">#</span> ...and deposition happened last year too.</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                stratigraphy[<span class="pl-s"><span class="pl-pds">&quot;</span>Stratum<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> stratum][idx:RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">=</span> currentdepth <span class="pl-c"><span class="pl-c">#</span> continue building current stratum</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>: <span class="pl-c"><span class="pl-c">#</span> ...but erosion happened last year.</span></td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                stratum <span class="pl-k">+=</span> <span class="pl-c1">1</span> <span class="pl-c"><span class="pl-c">#</span> make new stratum</span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                stratigraphy[<span class="pl-s"><span class="pl-pds">&quot;</span>Stratum<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> stratum] <span class="pl-k">=</span> <span class="pl-c1">0.0</span> <span class="pl-c"><span class="pl-c">#</span> add a column for the new stratum</span></td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                stratigraphy[<span class="pl-s"><span class="pl-pds">&quot;</span>Stratum<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> stratum][idx:RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">=</span> currentdepth <span class="pl-c"><span class="pl-c">#</span> begin building new stratum</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: <span class="pl-c"><span class="pl-c">#</span> Erosion happened this year...</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> key <span class="pl-k">in</span> stratigraphy.keys(): <span class="pl-c"><span class="pl-c">#</span>loop through strata</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> stratigraphy[key][idx] <span class="pl-k">&gt;</span> currentdepth: <span class="pl-c"><span class="pl-c">#</span> do we need to erode an old stratum?</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">                    stratigraphy[key][idx:RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>] <span class="pl-k">=</span> currentdepth <span class="pl-c"><span class="pl-c">#</span>erode!</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        old_delta <span class="pl-k">=</span> row[<span class="pl-s"><span class="pl-pds">&quot;</span>Delta<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>loop is done, make some figs!</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>make stacked bar plot</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Making temporal stratigraphic plot...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">plt.ioff() <span class="pl-c"><span class="pl-c">#</span> explicitly set interactive plotting off</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>set up styles with seaborn</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">sns.set_style(<span class="pl-s"><span class="pl-pds">&quot;</span>ticks<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">sns.set_context(<span class="pl-s"><span class="pl-pds">&quot;</span>poster<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font_scale</span> <span class="pl-k">=</span> <span class="pl-c1">1.1</span>)</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">colors <span class="pl-k">=</span> sns.cubehelix_palette(stratum<span class="pl-k">+</span><span class="pl-c1">1</span>, <span class="pl-v">start</span><span class="pl-k">=</span><span class="pl-c1">.75</span>, <span class="pl-v">rot</span><span class="pl-k">=</span><span class="pl-c1">1.5</span>, <span class="pl-v">dark</span><span class="pl-k">=</span><span class="pl-c1">.25</span>)</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">fig, ax <span class="pl-k">=</span> plt.subplots(<span class="pl-v">figsize</span><span class="pl-k">=</span>(<span class="pl-c1">17</span>, <span class="pl-c1">8</span>)) <span class="pl-c"><span class="pl-c">#</span>make blank plot, and set x and y axis limits to the maximum values in the stratigraphy array, and set a wide aspect ratio for the plot</span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">ax.set_autoscale_on(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>## <span class="pl-k">NOTE</span>: We have to &quot;trick&quot; the plot to get it look like values are measured as below surface. We will actually transform the values to be from below the surface after the plot is made....</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> strat <span class="pl-k">in</span> <span class="pl-c1">reversed</span>(<span class="pl-c1">range</span>(stratum<span class="pl-k">+</span><span class="pl-c1">1</span>)):</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    ax.bar(<span class="pl-c1">range</span>(RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>), stratigraphy.ix[:,strat], <span class="pl-v">width</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">color</span><span class="pl-k">=</span>colors[strat], <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Stratum <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> strat, <span class="pl-v">bottom</span><span class="pl-k">=</span><span class="pl-c1">0</span><span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength])</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">ax.plot(layers.Delta.cumsum()<span class="pl-k">+</span>initdepth<span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength], <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0.35<span class="pl-pds">&#39;</span></span>, <span class="pl-v">drawstyle</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>steps-post<span class="pl-pds">&quot;</span></span>, <span class="pl-v">linestyle</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>solid<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1.5</span>) <span class="pl-c"><span class="pl-c">#</span> plot the outline of where the surface has been</span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">ax.plot((<span class="pl-c1">0</span>, RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>), (<span class="pl-c1">0</span>,<span class="pl-c1">0</span>), <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>black<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dashed<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1.75</span>) <span class="pl-c"><span class="pl-c">#</span> plot a horizontal line for modern day surface</span></td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">ax.plot((<span class="pl-c1">0</span>, RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>), (initdepth<span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength],initdepth<span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength]), <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0.35<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linestyle</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dotted<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1.75</span>) <span class="pl-c"><span class="pl-c">#</span> plot a horizontal line for original surface</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">ax.text(<span class="pl-c1">5</span>, <span class="pl-c1">0.02</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Final Surface<span class="pl-pds">&quot;</span></span>, <span class="pl-v">bbox</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">facecolor</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>white<span class="pl-pds">&#39;</span></span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.25</span>))<span class="pl-c"><span class="pl-c">#</span> add lables for the horizontal lines</span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">ax.text(<span class="pl-c1">5</span>, initdepth<span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength] <span class="pl-k">+</span> <span class="pl-c1">0.02</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Initial Surface<span class="pl-pds">&quot;</span></span>,<span class="pl-v">bbox</span><span class="pl-k">=</span><span class="pl-c1">dict</span>(<span class="pl-v">facecolor</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>white<span class="pl-pds">&#39;</span></span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.25</span>))</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">ax.locator_params(<span class="pl-v">nbins</span> <span class="pl-k">=</span> <span class="pl-c1">8</span>)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">ax.set_xlim(<span class="pl-c1">0</span>,RunLength<span class="pl-k">+</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">ax.set_ylim(miny,np.amax(np.amax(stratigraphy))<span class="pl-k">-</span>stratigraphy.ix[:,stratum][RunLength])</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">plt.xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Year<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">plt.ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Depth below last surface (m)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">ax.legend(<span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center left<span class="pl-pds">&#39;</span></span>, <span class="pl-v">bbox_to_anchor</span><span class="pl-k">=</span>(<span class="pl-c1">1.015</span>, <span class="pl-c1">0.5</span>), <span class="pl-v">fontsize</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>small<span class="pl-pds">&#39;</span></span>, <span class="pl-v">frameon</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>True<span class="pl-pds">&#39;</span></span>, <span class="pl-v">shadow</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>True<span class="pl-pds">&#39;</span></span>, <span class="pl-v">fancybox</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>True<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">fig.subplots_adjust(<span class="pl-v">left</span><span class="pl-k">=</span><span class="pl-c1">0.065</span>, <span class="pl-v">right</span><span class="pl-k">=</span><span class="pl-c1">0.90</span>)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">sns.despine(fig)</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_stratigraphy_stackedbar.png<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix, <span class="pl-v">dpi</span><span class="pl-k">=</span><span class="pl-c1">300</span>)</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">plt.close()</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">mbsstrat <span class="pl-k">=</span> (stratigraphy <span class="pl-k">-</span> stratigraphy.ix[:,stratum][RunLength]) <span class="pl-c"><span class="pl-c">#</span> NOW change the stratigraphy to depth below surface, </span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">mbsstrat.T.to_csv(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_stratigraphy.csv<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix) <span class="pl-c"><span class="pl-c">#</span> transpose, and save it out to a file</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>loop through the data to make a final proxy count</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Accumulating proxy-data by depth increments...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">proxylist <span class="pl-k">=</span> [] <span class="pl-c"><span class="pl-c">#</span> set up a list to contain results</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> idx, row <span class="pl-k">in</span> layers.iterrows():</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>: <span class="pl-c"><span class="pl-c">#</span> Deposition occured, so accumulate proxies and depth</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">        numdepths <span class="pl-k">=</span> <span class="pl-c1">int</span>(row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-k">/</span> baseinterval) <span class="pl-c"><span class="pl-c">#</span> findout how many depth intervals to add</span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> depth <span class="pl-k">in</span> <span class="pl-c1">range</span>(numdepths): <span class="pl-c"><span class="pl-c">#</span> now add the correct proportion of proxy to each interval</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">            proxylist.append([row[<span class="pl-s"><span class="pl-pds">&#39;</span>InSitu Grass Phytoliths<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span>numdepths, row[<span class="pl-s"><span class="pl-pds">&#39;</span>Scaled Basin-Average Grass Phytoliths<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span>numdepths, row[<span class="pl-s"><span class="pl-pds">&#39;</span>InSitu Charcoal<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span>numdepths, row[<span class="pl-s"><span class="pl-pds">&#39;</span>Scaled Basin-Average Charcoal<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span>numdepths, row[<span class="pl-s"><span class="pl-pds">&#39;</span>Artifacts<span class="pl-pds">&#39;</span></span>]<span class="pl-k">/</span>numdepths])</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&lt;</span> <span class="pl-c1">0</span>: <span class="pl-c"><span class="pl-c">#</span> Erosion occured, so remove proxies and depth</span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">        numdepths <span class="pl-k">=</span> <span class="pl-c1">int</span>(row[<span class="pl-s"><span class="pl-pds">&#39;</span>Delta<span class="pl-pds">&#39;</span></span>] <span class="pl-k">/</span> baseinterval) <span class="pl-c"><span class="pl-c">#</span> findout how many depth intervals to remove</span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> depth <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">abs</span>(numdepths)): <span class="pl-c"><span class="pl-c">#</span> now remove the correct number of intervals, including all their proxy data</span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                proxylist.pop()</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>(<span class="pl-c1">IndexError</span>):</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>: <span class="pl-c"><span class="pl-c">#</span> no change happened, so pass on by</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> idx, i <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(proxylist):</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">    i.append((idx<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">*-</span><span class="pl-c1">1</span><span class="pl-k">*</span>baseinterval) <span class="pl-c"><span class="pl-c">#</span> add cumualtive depth intervals</span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">proxyframe <span class="pl-k">=</span> pd.DataFrame(np.array(proxylist)) <span class="pl-c"><span class="pl-c">#</span> convert to dataframe via np array</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">labels <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Grass Phyt, insitu<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Grass Phyt, bas. av.<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Macrocharcoal, insitu<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Macrocharcoal, bas. av.<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Artifacts<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Depth<span class="pl-pds">&quot;</span></span>] <span class="pl-c"><span class="pl-c">#</span> create some column labels (will also be used in the plot)</span></td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">proxyframe.columns <span class="pl-k">=</span> labels <span class="pl-c"><span class="pl-c">#</span> add column labels to proxyframe</span></td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">proxyframe.to_csv(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_raw_proxies.csv<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix) <span class="pl-c"><span class="pl-c">#</span> save out the raw proxies dataframe to csv file</span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Creating proxy depth plot...<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">accumprox <span class="pl-k">=</span> proxyframe.groupby(np.arange(<span class="pl-c1">len</span>(proxyframe))<span class="pl-k">//</span>dispinterval).sum() <span class="pl-c"><span class="pl-c">#</span> aggregate data to the binned display interval (for the plot)</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">accumprox.drop(<span class="pl-s"><span class="pl-pds">&#39;</span>Depth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">inplace</span><span class="pl-k">=</span><span class="pl-c1">True</span>) <span class="pl-c"><span class="pl-c">#</span> the depth column is now bad due to the summing operation above, remove it</span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">accumprox[<span class="pl-s"><span class="pl-pds">&#39;</span>Depth<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> np.arange(<span class="pl-c1">1</span>,<span class="pl-c1">len</span>(accumprox)<span class="pl-k">+</span><span class="pl-c1">1</span>)<span class="pl-k">*</span>(<span class="pl-k">-</span><span class="pl-c1">1</span><span class="pl-k">*</span>baseinterval<span class="pl-k">*</span>dispinterval)  <span class="pl-c"><span class="pl-c">#</span> Make new depth column with corrected values.</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> make a plot of the proxies with depth</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">deletethis <span class="pl-k">=</span> labels.pop() <span class="pl-c"><span class="pl-c">#</span> just peel off the Depth label so we can use the rest of the labels for the plots.</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">xlabs <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>g/cc<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>g/cc<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>pieces/cc<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>pieces/cc<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>pieces/cc<span class="pl-pds">&quot;</span></span>] <span class="pl-c"><span class="pl-c">#</span> labels for the xaxes in the plot. Need to have same number as there are plots.</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">sns.set_style(<span class="pl-s"><span class="pl-pds">&quot;</span>ticks<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">sns.set_context(<span class="pl-s"><span class="pl-pds">&quot;</span>poster<span class="pl-pds">&quot;</span></span>, <span class="pl-v">font_scale</span> <span class="pl-k">=</span> <span class="pl-c1">1.1</span>)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">fig, axes <span class="pl-k">=</span> plt.subplots(<span class="pl-v">nrows</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">ncols</span><span class="pl-k">=</span><span class="pl-c1">len</span>(labels), <span class="pl-v">sharey</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">sharex</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">figsize</span><span class="pl-k">=</span>(<span class="pl-c1">18</span>, <span class="pl-c1">8</span>)) <span class="pl-c"><span class="pl-c">#</span>make blank plot, and set size</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> color, lab, xlab, ax <span class="pl-k">in</span> <span class="pl-c1">zip</span>(sns.cubehelix_palette(<span class="pl-c1">len</span>(labels), <span class="pl-v">start</span><span class="pl-k">=</span><span class="pl-c1">.75</span>, <span class="pl-v">rot</span><span class="pl-k">=</span><span class="pl-c1">1.5</span>, <span class="pl-v">dark</span><span class="pl-k">=</span><span class="pl-c1">.25</span>), labels, xlabs, axes):</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">    ax.barh(accumprox.Depth, accumprox[lab], <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">.09</span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">color</span><span class="pl-k">=</span>color)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">    ax.set_title(lab, <span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">    ax.set_xscale(proxyscale)</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">    ax.set_xlim(<span class="pl-v">xmin</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">    ax.set_ylim([np.amin(accumprox.Depth), <span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    ax.set_xlabel(xlab)</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">    ax.locator_params(<span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>, <span class="pl-v">nbins</span><span class="pl-k">=</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">    ax.patch.set_visible(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> item <span class="pl-k">in</span> mbsstrat.T[RunLength]:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">        ax.axhline(<span class="pl-v">y</span><span class="pl-k">=</span>item, <span class="pl-v">xmin</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">xmax</span><span class="pl-k">=</span><span class="pl-c1">1.5</span>, <span class="pl-v">c</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0.75<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">zorder</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">clip_on</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span>ax.plot((0, np.amax(accumprox[lab])), (item,item), color=&#39;black&#39;, linestyle=&#39;dashed&#39;, linewidth=1, clip_on=False) # plot a horizontal line for modern day surface</span></td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>fig.text(0.5, 0.02, &#39;Amount of proxy (counts or weights)&#39;, ha=&#39;center&#39;, va=&#39;center&#39;, fontsize=18)</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">fig.text(<span class="pl-c1">0.04</span>, <span class="pl-c1">0.5</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Depth Below Surface (m)<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ha</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center<span class="pl-pds">&#39;</span></span>, <span class="pl-v">va</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center<span class="pl-pds">&#39;</span></span>, <span class="pl-v">rotation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>vertical<span class="pl-pds">&#39;</span></span>, <span class="pl-v">fontsize</span><span class="pl-k">=</span><span class="pl-c1">18</span>)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">fig.subplots_adjust(<span class="pl-v">bottom</span><span class="pl-k">=</span><span class="pl-c1">0.11</span>, <span class="pl-v">right</span><span class="pl-k">=</span><span class="pl-c1">0.95</span>, <span class="pl-v">wspace</span><span class="pl-k">=</span><span class="pl-c1">0.35</span>)</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">plt.locator_params(<span class="pl-v">axis</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>, <span class="pl-v">nbins</span> <span class="pl-k">=</span> <span class="pl-c1">len</span>(accumprox))</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>plt.locator_params(axis = &#39;x&#39;, nbins = 4)</span></td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">sns.despine()</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_proxies_barplot.png<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix, <span class="pl-v">dpi</span><span class="pl-k">=</span><span class="pl-c1">300</span>)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">plt.close()</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">accumprox.to_csv(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_binned_proxies.csv<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix) <span class="pl-c"><span class="pl-c">#</span> save out the binned proxies dataframe to csv file</span></td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">fig, axes <span class="pl-k">=</span> plt.subplots(<span class="pl-v">nrows</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">ncols</span><span class="pl-k">=</span><span class="pl-c1">3</span>, <span class="pl-v">sharey</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">sharex</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">figsize</span><span class="pl-k">=</span>(<span class="pl-c1">14</span>, <span class="pl-c1">8</span>)) <span class="pl-c"><span class="pl-c">#</span>make blank plot, and set size</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line"><span class="pl-k">for</span> color, lab, xlab, ax <span class="pl-k">in</span> <span class="pl-c1">zip</span>((<span class="pl-s"><span class="pl-pds">&#39;</span>yellow<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>green<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>blue<span class="pl-pds">&#39;</span></span>), (labels[<span class="pl-c1">1</span>],labels[<span class="pl-c1">3</span>],labels[<span class="pl-c1">4</span>]), (xlabs[<span class="pl-c1">1</span>],xlabs[<span class="pl-c1">3</span>],xlabs[<span class="pl-c1">4</span>]), axes):</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">    ax.barh(accumprox.Depth, accumprox[lab], <span class="pl-v">height</span><span class="pl-k">=</span><span class="pl-c1">.09</span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">color</span><span class="pl-k">=</span>color)</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">    ax.set_title(lab, <span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    ax.set_xscale(proxyscale)</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    ax.set_xlim(<span class="pl-v">xmin</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">    ax.set_ylim([np.amin(accumprox.Depth), <span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">    ax.set_xlabel(xlab)</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    ax.locator_params(<span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>x<span class="pl-pds">&#39;</span></span>, <span class="pl-v">nbins</span><span class="pl-k">=</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    ax.patch.set_visible(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> item <span class="pl-k">in</span> mbsstrat.T[RunLength]:</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        ax.axhline(<span class="pl-v">y</span><span class="pl-k">=</span>item, <span class="pl-v">xmin</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">xmax</span><span class="pl-k">=</span><span class="pl-c1">1.5</span>, <span class="pl-v">c</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0.75<span class="pl-pds">&#39;</span></span>, <span class="pl-v">linewidth</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">zorder</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">clip_on</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span>ax.plot((0, np.amax(accumprox[lab])), (item,item), color=&#39;black&#39;, linestyle=&#39;dashed&#39;, linewidth=1, clip_on=False) # plot a horizontal line for modern day surface</span></td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>fig.text(0.5, 0.02, &#39;Amount of proxy (counts or weights)&#39;, ha=&#39;center&#39;, va=&#39;center&#39;, fontsize=18)</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">fig.text(<span class="pl-c1">0.04</span>, <span class="pl-c1">0.5</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>Depth Below Surface (m)<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ha</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center<span class="pl-pds">&#39;</span></span>, <span class="pl-v">va</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>center<span class="pl-pds">&#39;</span></span>, <span class="pl-v">rotation</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>vertical<span class="pl-pds">&#39;</span></span>, <span class="pl-v">fontsize</span><span class="pl-k">=</span><span class="pl-c1">18</span>)</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">fig.subplots_adjust(<span class="pl-v">bottom</span><span class="pl-k">=</span><span class="pl-c1">0.11</span>, <span class="pl-v">right</span><span class="pl-k">=</span><span class="pl-c1">0.95</span>, <span class="pl-v">wspace</span><span class="pl-k">=</span><span class="pl-c1">0.35</span>)</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">plt.locator_params(<span class="pl-v">axis</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span>, <span class="pl-v">nbins</span> <span class="pl-k">=</span> <span class="pl-c1">len</span>(accumprox))</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>plt.locator_params(axis = &#39;x&#39;, nbins = 4)</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">sns.despine()</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_basav_proxies_barplot.png<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix, <span class="pl-v">dpi</span><span class="pl-k">=</span><span class="pl-c1">300</span>)</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">plt.close()</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">accumprox.to_csv(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_binned_proxies.csv<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> outprefix) <span class="pl-c"><span class="pl-c">#</span> save out the binned proxies dataframe to csv file</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">grass.message(<span class="pl-s"><span class="pl-pds">&quot;</span>Finished!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy class="dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" href="/comses/medland/blame/6ab47b971a35fb88f3a1e0a880f7a323e4133df5/digital_proxy_model/strat_column.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" href="/comses/medland/issues/new">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.41147s from unicorn-3114010823-x2v33">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to blog, text:blog" href="https://github.com/blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-gEAdDZ4LgyEE51A6EiCI5F8hC2pELVwJzk9fcRYT6JKNg92wpQhso4uD1rML8kTVE8FFW4G1hKIm+eWgX+D5/g==" type="application/javascript" src="https://assets-cdn.github.com/assets/compat-432e5bb0f7cc942dbf63a7c74de5da3c.js"></script>
    <script crossorigin="anonymous" integrity="sha512-bDFUXMGHFddte8PoN8CW5xNr/0w/9Zrfsjun90gr7lJdc7w5+NLGNrJHTPFeaZa5ph1MzSTQg7fqTg/CI95fSw==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-c566e2adb34ea4706cec5d285e57dd1d.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-YtM20V79jshLTZftClKMk0TEp49UOfrjsI4gsA5918LlX0Pk8403/gXznbgRy5z6TyLC7UEMSHwfRe9ZfqB/OQ==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-f6e573faaf4bc3bb877e6edffb9ed177.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>


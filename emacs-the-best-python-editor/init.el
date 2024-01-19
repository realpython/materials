;; .emacs.d/init.el

;; MELPA Package Support
(require 'package)

;; Adds the Melpa archive to the list of available repositories
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/") t)

;; Initializes the package infrastructure
(package-initialize)

;; If there are no archived package contents, refresh them
(when (not package-archive-contents)
  (package-refresh-contents))

;; List of packages to install
(defvar myPackages
  '(better-defaults
    elpy
    ein
    flycheck
    py-autopep8
    blacken
    magit
    material-theme))

;; Install packages if not already installed
(dolist (package myPackages)
  (unless (package-installed-p package)
    (package-install package)))

;; Set the path to virtualenvwrapper.sh
(setq py-which-bufname " *virtualenvwrapper*")
(setq py-virtualenvwrapper-works-p t)
(setq py-virtualenvwrapper-exec-path "/home/vagrant/.local/lib/python3.8/site-packages/virtualenvwrapper.sh")

;; Basic Customization
(setq inhibit-startup-message t)  ;; Hide the startup message
(load-theme 'material t)          ;; Load material theme
(global-linum-mode t)             ;; Enable line numbers globally

;; Development Setup
(elpy-enable)  ;; Enable elpy

;; Set Python indentation offset
(setq python-indent-offset 4) ; You can change 4 to your preferred indentation level

;; Disable dedicated virtualenv path (use 'current' for the current project directory)
(setq elpy-rpc-virtualenv-path 'current)

;; Enable Flycheck
(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

;; User-Defined init.el ends here

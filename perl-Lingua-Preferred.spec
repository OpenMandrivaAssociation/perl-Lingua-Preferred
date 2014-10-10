%define module	Lingua-Preferred
%define version	0.2.4
%define release 9

Summary:	Perl extension to choose a language
License:	GPL/Artistic
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	perl(Log::TraceMessages)
BuildRequires:	perl-devel


%description
Often human-readable information is available in more than one language. Which
should you use? This module provides a way for the user to specify possible
languages in order of preference, and then to pick the best language of those
available. Different 'dialects' given by the 'territory' part of the language
specifier (such as en, en_GB, and en_US) are also supported.

Authors:
--------
        Ed Avis <epa98@doc.ic.ac.uk>

%prep
%setup -n %{module}-%{version} -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Lingua/Preferred.pm
%{perl_vendorlib}/auto/Lingua/Preferred/autosplit.ix
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.4-8mdv2010.0
+ Revision: 430480
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2.4-7mdv2009.0
+ Revision: 257563
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.4-6mdv2009.0
+ Revision: 245623
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.4-4mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.2.4-4mdv2007.0
+ Revision: 103812
- Import perl-Lingua-Preferred

* Fri May 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.4-4mdk
- Fix BuildRequires
- Fix Build 
- Fix Source URL
- Fix URL

* Fri Apr 22 2005 Stefan van der Eijk <stefan@eijk.nu> 0.2.4-3mdk
- mkrel
- reupload (stuff got lost)

* Mon Feb 28 2005 Stefan van der Eijk <stefan@eijk.nu> 0.2.4-2mdk
- B'day rebuild
- use AutoReqProv

* Sun Jan 11 2004 Stefan van der Eijk <stefan@eijk.nu> 0.2.4-1mdk
- 0.2.4

